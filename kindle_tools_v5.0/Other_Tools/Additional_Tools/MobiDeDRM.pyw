#!/usr/bin/env python
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

import sys
sys.path.append('lib')
import os, os.path, urllib
import subprocess
from subprocess import Popen, PIPE, STDOUT
import subasyncio
from subasyncio import Process
import Tkinter
import Tkconstants
import tkFileDialog
import tkMessageBox
from scrolltextwidget import ScrolledText

class MainDialog(Tkinter.Frame):
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root, border=5)
        self.root = root
        self.interval = 2000
        self.p2 = None
        self.status = Tkinter.Label(self, text='Remove Encryption from a Mobi eBook')
        self.status.pack(fill=Tkconstants.X, expand=1)
        body = Tkinter.Frame(self)
        body.pack(fill=Tkconstants.X, expand=1)
        sticky = Tkconstants.E + Tkconstants.W
        body.grid_columnconfigure(1, weight=2)

        Tkinter.Label(body, text='Mobi eBook input file').grid(row=0, sticky=Tkconstants.E)
        self.mobipath = Tkinter.Entry(body, width=50)
        self.mobipath.grid(row=0, column=1, sticky=sticky)
        cwd = os.getcwdu()
        cwd = cwd.encode('utf-8')
        self.mobipath.insert(0, cwd)
        button = Tkinter.Button(body, text="...", command=self.get_mobipath)
        button.grid(row=0, column=2)

        Tkinter.Label(body, text='Name for Unencrypted Output File').grid(row=1, sticky=Tkconstants.E)
        self.outpath = Tkinter.Entry(body, width=50)
        self.outpath.grid(row=1, column=1, sticky=sticky)
        self.outpath.insert(0, '')
        button = Tkinter.Button(body, text="...", command=self.get_outpath)
        button.grid(row=1, column=2)

        Tkinter.Label(body, text='10 Character PID').grid(row=2, sticky=Tkconstants.E)
        self.pidnum = Tkinter.StringVar()
        self.pidinfo = Tkinter.Entry(body, width=12, textvariable=self.pidnum)
        self.pidinfo.grid(row=2, column=1, sticky=sticky)

        msg1 = 'Conversion Log \n\n'
        self.stext = ScrolledText(body, bd=5, relief=Tkconstants.RIDGE, height=15, width=60, wrap=Tkconstants.WORD)
        self.stext.grid(row=3, column=0, columnspan=2,sticky=sticky)
        self.stext.insert(Tkconstants.END,msg1)

        buttons = Tkinter.Frame(self)
        buttons.pack()
        self.sbotton = Tkinter.Button(
            buttons, text="Start", width=10, command=self.convertit)
        self.sbotton.pack(side=Tkconstants.LEFT)

        Tkinter.Frame(buttons, width=10).pack(side=Tkconstants.LEFT)
        self.qbutton = Tkinter.Button(
            buttons, text="Quit", width=10, command=self.quitting)
        self.qbutton.pack(side=Tkconstants.RIGHT)

    # read from subprocess pipe without blocking
    # invoked every interval via the widget "after"
    # option being used, so need to reset it for the next time
    def processPipe(self):
        poll = self.p2.wait('nowait')
        if poll != None: 
            text = self.p2.readerr()
            text += self.p2.read()
            msg = text + '\n\n' + 'Encryption successfully removed\n'
            if poll != 0:
                msg = text + '\n\n' + 'Error: Encryption Removal Failed\n'
            self.showCmdOutput(msg)
            self.p2 = None
            self.sbotton.configure(state='normal')
            return
        text = self.p2.readerr()
        text += self.p2.read()
        self.showCmdOutput(text)
        # make sure we get invoked again by event loop after interval 
        self.stext.after(self.interval,self.processPipe)
        return

    # post output from subprocess in scrolled text widget
    def showCmdOutput(self, msg):
        if msg and msg !='':
            msg = msg.encode('utf-8')
            if sys.platform.startswith('win'):
                msg = msg.replace('\r\n','\n')
            self.stext.insert(Tkconstants.END,msg)
            self.stext.yview_pickplace(Tkconstants.END)
        return

    # run as a subprocess via pipes and collect stdout
    def mobirdr(self, infile, outfile, pidnum):
        # os.putenv('PYTHONUNBUFFERED', '1')
        cmdline = 'python ./lib/mobidedrm.py "' + infile + '" "' + outfile + '" "' + pidnum + '"'
        if sys.platform[0:3] == 'win':
            search_path = os.environ['PATH']
            search_path = search_path.lower()
            if search_path.find('python') >= 0: 
                cmdline = 'python lib\mobidedrm.py "' + infile + '" "' + outfile + '" "' + pidnum + '"'
            else :
                cmdline = 'lib\mobidedrm.py "' + infile + '" "' + outfile + '" "' + pidnum + '"'

        cmdline = cmdline.encode(sys.getfilesystemencoding())
        p2 = Process(cmdline, shell=True, bufsize=1, stdin=None, stdout=PIPE, stderr=PIPE, close_fds=False)
        return p2


    def get_mobipath(self):
        mobipath = tkFileDialog.askopenfilename(
            parent=None, title='Select Mobi eBook File',
            defaultextension='.prc', filetypes=[('Mobi eBook File', '.prc'), ('Mobi eBook File', '.azw'),('Mobi eBook File', '.mobi'),
                                                ('All Files', '.*')])
        if mobipath:
            mobipath = os.path.normpath(mobipath)
            self.mobipath.delete(0, Tkconstants.END)
            self.mobipath.insert(0, mobipath)
        return

    def get_outpath(self):
        mobipath = self.mobipath.get()
        initname = os.path.basename(mobipath)
        p = initname.find('.')
        if p >= 0: initname = initname[0:p]
        initname += '_nodrm.mobi' 
        outpath = tkFileDialog.asksaveasfilename(
            parent=None, title='Select Unencrypted Mobi File to produce',
            defaultextension='.mobi', initialfile=initname,
            filetypes=[('Mobi files', '.mobi'), ('All files', '.*')])
        if outpath:
            outpath = os.path.normpath(outpath)
            self.outpath.delete(0, Tkconstants.END)
            self.outpath.insert(0, outpath)
        return

    def quitting(self):
        # kill any still running subprocess
        if self.p2 != None:
            if (self.p2.wait('nowait') == None):
                self.p2.terminate()
        self.root.destroy()

    # actually ready to run the subprocess and get its output
    def convertit(self):
        # now disable the button to prevent multiple launches
        self.sbotton.configure(state='disabled')
        mobipath = self.mobipath.get()
        outpath = self.outpath.get()
        pidnum = self.pidinfo.get()
        if not mobipath or not os.path.exists(mobipath):
            self.status['text'] = 'Specified Mobi eBook file does not exist'
            self.sbotton.configure(state='normal')
            return
        if not outpath:
            self.status['text'] = 'No output file specified'
            self.sbotton.configure(state='normal')
            return
        if not pidnum or pidnum == '':
            self.status['text'] = 'No PID specified'
            self.sbotton.configure(state='normal')
            return

        log = 'Command = "python mobidedrm.py"\n'
        log += 'Mobi Path = "'+ mobipath + '"\n'
        log += 'Output File = "' + outpath + '"\n'
        log += 'PID = "' + pidnum + '"\n'
        log += '\n\n'
        log += 'Please Wait ...\n\n'
        log = log.encode('utf-8')
        self.stext.insert(Tkconstants.END,log)
        self.p2 = self.mobirdr(mobipath, outpath, pidnum)

        # python does not seem to allow you to create
        # your own eventloop which every other gui does - strange 
        # so need to use the widget "after" command to force
        # event loop to run non-gui events every interval
        self.stext.after(self.interval,self.processPipe)
        return


def main(argv=None):
    root = Tkinter.Tk()
    root.title('Mobi eBook Encryption Removal')
    root.resizable(True, False)
    root.minsize(300, 0)
    MainDialog(root).pack(fill=Tkconstants.X, expand=1)
    root.mainloop()
    return 0
    

if __name__ == "__main__":
    sys.exit(main())
