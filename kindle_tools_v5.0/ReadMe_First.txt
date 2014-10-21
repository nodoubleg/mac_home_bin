Welcome to the tools!
=====================

This ReadMe_First.txt is meant to give users a quick overview of what is available and how to get started. 

The is archive includes tools to remove DRM from:
 - eReader PDB books
 - Barnes and Noble ePubs
 - Adobe Digitial Editions ePubs
 - Adobe Digitial Editions PDFs
 - Kindle/Mobipocket ebooks (including Topaz, Print Replica and KF8).

These tools do NOT work with Apple's iBooks FairPlay DRM.

The only tool that removes Apple's iBooks Fairplay DRM that is Requiem by Brahms version 3.3 or later. Requiem is NOT included in this tools package. It is under active development because Apple constantly updates its DRM scheme to stop Requiem from working.

Requiem has a Tor website: http://tag3ulp55xczs3pn.onion. To reach the site using Tor, you will need to install Tor (http://www.torproject.org). If you're willing to sacrifice your anonymity, you can use the regular web with tor2web. Just go to http://tag3ulp55xczs3pn.tor2web.com.



Calibre Users (Mac OS X, Windows, and Linux)
--------------------------------------------
If you are a calibre user, the quickest and easiest way to remove DRM from your ebooks is to open the Calibre_Plugins folder and install each of the plugins following the instructions and configuration directions provided in each plugins' README file.

Once installed and configured, you can simply add a DRM book to calibre and the DeDRM version will be imported into the calibre database. Note that DRM removal ONLY occurs on import. If you have already imported DRM books you'll need to remove them from calibre and re-import them.

These plugins work for Windows and Mac OS X. All plugins (including the K4MobiDeDRM plugin when used on books from Kindle for PC under wine) should also work on Linux. Linux users should read the section at the end of this ReadMe.



DeDRM Application for Mac OS X Users: (Mac OS X 10.5, 10.6, and 10.7)
----------------------------------------------------------------------
From the DeDRM_Applications folder, drag the DeDRM_X.X.app.zip droplet to your Desktop. Double-click on it once to unzip it to create the DeDRM X.X.app droplet. Double-click on the droplet once and it will guide you through collecting the data it needs to remove the DRM.

To use it simply drag ebooks or folders containing ebooks onto the DeDRM X.X.app droplet and it will process the ebooks.



DeDRM Application for Windows Users: (Windows XP through Windows 7)
------------------------------------------------------------------
***This program requires that Python and PyCrypto be properly installed***.
See below for details on which versions are recommended.

From the DeDRM_Applications folder, fully extract the DeDRM_vX.X_WinApp.zip. Drag the resulting DeDRM_vx.x_WinApp folder to someplace out of the way on your machine. Open the folder and make a short-cut from the DeDRM_Drop_Target onto your Desktop. Double-click on the short-cut and DeDRM will launch and it will guide you through collecting the data it needs to remove the DRM. 

To use it simply drag ebooks or folders containing ebooks onto the DeDRM_Drop_Target short-cut, and it will process the ebooks.



Other_Tools
-----------
There are a number of other python based tools that have graphical user interfaces to make them easy to use. To use any of these tools, you need to have Python 2.5, 2.6, or 2.7 for 32 bits installed on your machine as well as a matching PyCrypto or OpenSSL for some tools.

On Mac OS X (10.5, 10.6 and 10.7), your systems already have the proper Python and OpenSSL installed. So nothing need be done, you can already run these tools by double-clicking on the .pyw python scripts.

Users of Mac OS X 10.3 and 10.4, need to download and install the "32-bit Mac Installer disk Image (2.7.X) for OS X 10.3 and later from http://www.python.org/download/releases/2.7.1/

On Windows, you need to install a 32 bit version of Python (even on Windows 64) plus a matching 32 bit version of PyCrypto *OR* OpenSSL. We ***strongly*** recommend the free community edition of ActiveState's Active Python version. See the end of this document for details.

Linux users should have python 2.7, and openssl installed. but may need to run some of these tools under recent versions of Wine. See the Linux_Users section below:

The scripts in the Other_Tools folder are organized by type of ebook you need to remove the DRM from. Choose from among:

  "Adobe_ePub_Tools"
  "Adobe_PDF_Tools"
  "Barnes_and_Noble_ePub_Tools"
  "eReader_PDB_Tools"
  "KindleBooks"
  "Kindle_for_Android_Patch"
  "ePub_Fixer" (for fixing incorrectly made Adobe and Barnes and Noble ePubs)

by simply opening that folder.

Look for a README inside of the relevant folder to get you started. 



Additional Tools
----------------
Some additional useful tools **unrelated to DRM** are also provided in the "Additional_Tools" folder. There are tools for working with finding Topaz ebooks, unpacking Kindle/Mobipocket ebooks (without DRM) to get to the Mobipocket markup language inside, tools to strip source archive from Kindlegen generated mobis, tools to work with Kindle for iPhone/iPad, etc, and tools to dump the contents of mobi headers to see all EXTH (metadata) and related values.



Windows and Python
------------------
We **strongly** recommend ActiveState's Active Python 2.7 Community Edition for Windows (x86) 32 bits. This can be downloaded for free from:

	http://www.activestate.com/activepython/downloads

We do **NOT** recommend the version of Python from python.org.

The version from python.org is not as complete as most normal Python installations on Linux and even Mac OS X. It is missing various Windows specific libraries, does not install the default Tk Widget kit (for graphical user interfaces) unless you select it as an option in the installer, and does not properly update the system PATH environment variable. Therefore using the default python.org build on Windows is simply an exercise in frustration for most Windows users.

In addition, Windows Users need one of PyCrypto OR OpenSSL.

For OpenSSL:

	Win32 OpenSSL v0.9.8o (8Mb)
	http://www.slproweb.com/download/Win32OpenSSL-0_9_8o.exe
	(if you get an error message about missing Visual C++
	redistributables... cancel the install and install the
	below support program from Microsoft, THEN install OpenSSL)

	Visual C++ 2008 Redistributables (1.7Mb)
	http://www.microsoft.com/downloads/details.aspx?familyid=9B2DA534-3E03-4391-8A4D-074B9F2BC1BF

For PyCrypto:

	There are many places to get PyCrypto installers for Windows. One such place is:

		http://www.voidspace.org.uk/python/modules.shtml

	Please get the latest PyCrypto meant for Windows 32 bit that matches the version of Python you installed (2.7)

Once Windows users have installed Python 2.X for 32 bits, and the matching OpenSSL OR PyCrypto pieces, they too are ready to run the scripts.





Linux Users Only
================

Since Kindle for PC and Adobe Digital Editions do not offer native Linux versions, here are instructions for using Windows versions under Wine as well as related instructions for the special way to handle some of these tools:


Linux and Kindle for PC (Other_Tools/KindleBooks/)
--------------------------------------------------

Here are the instructions for using Kindle for PC and KindleBooks.pyw on Linux under Wine. (Thank you Eyeless and Pete)

1. upgrade to very recent versions of Wine; This has been tested with Wine 1.3.15 – 1.3.2X. It may work with earlier versions but no promises. It does not work with wine 1.2.X versions.

If you have not already installed Kindle for PC under wine, follow steps 2 and 3 otherwise jump to step 4

2. Some versions of winecfg have a bug in setting the volume serial number, so create a .windows-serial file at root of drive_c to set a proper windows volume serial number (8 digit hex value for unsigned integer).
cd ~
cd .wine
cd drive_c
echo deadbeef > .windows-serial 

Replace "deadbeef" with whatever hex value you want but I would stay away from the default setting of "ffffffff" which does not seem to work. BTW: deadbeef is itself a valid possible hex value if you want to use it

3. Only ***after*** setting the volume serial number properly – download and install under wine K4PC version for Windows. Register it and download from your Archive one of your Kindle ebooks. Versions known to work are K4PC 1.7.1 and earlier. Later version may work but no promises.

4. Download and install under wine ActiveState Active Python 2.7 for Windows 32bit

5. Download and unzip tools_vX.X.zip

6. Now make sure the executable bit is NOT set for KindleBooks.pyw as Linux will actually keep trying to ignore wine and launch it under Linux python which will cause it to fail.

cd tools_vX.X/KindleBooks/
chmod ugo-x KindleBooks.pyw

7. Then run KindleBook.pyw ***under python running on wine*** using the Linux shell as follows:

wine python KindleBooks.pyw

Select the ebook file directly from your “My Kindle Content” folder, select a new/unused directory for the output. You should not need to enter any PID or Serial Number for Kindle for PC.




Linux and Adobe Digital Editions ePubs
--------------------------------------

Here are the instructions for using the tools with ePub books and Adobe Digital Editions on Linux under Wine. (Thank you mclien!)


1. download the most recent version of wine from winehq.org (1.3.29 in my case)

For debian users: 

to get a recent version of wine I decited to use aptosid (2011-02, xfce)
(because I’m used to debian)
install aptosid and upgrade it (see aptosid site for detaild instructions)


2. properly install Wine (see the Wine site for details)

For debian users:

cd to this dir and install the packages as root:
‘dpkg -i *.deb’ 
you will get some error messages, which can be ignored.
again as root use
‘apt-get -f install’ to correct this errors

3. python 2.7 should already be installed on your system but you may need the following additional python package

'apt-get install python-tk’

4. all programms need to be installed as normal user. All these programm are installed the same way:
‘wine ‘
we need:
a) Adobe Digital Edition 1.7.2(from: http://kb2.adobe.com/cps/403/kb403051.html)
(there is a “can’t install ADE” site, where the setup.exe hides)

b) ActivePython-2.7.2.5-win32-x86.msi (from: http://www.activestate.com/activepython/downloads)

c) Win32OpenSSL_Light-0_9_8r.exe (from: http://www.slproweb.com/)

d) pycrypto-2.3.win32-py2.7.msi (from: http://www.voidspace.org.uk/python/modules.shtml)

5. now get and unpack the very latest tools_vX.X (from Apprentice Alf) in the users drive_c of wine
(~/.wine/drive_c/)

6. start ADE with:
‘wine digitaleditions.exe’ or from the start menue wine-adobe-digital..

7. register this instance of ADE with your adobeID and close it
 change to the tools_vX.X dir:
cd ~/.wine/drive_c/tools_vX.X/Other_Tools/Adobe_ePub_Tools

8. create the adeptkey.der with:
‘wine python ineptkey_v5.4.pyw’ (only need once!)
(key will be here: ~/.wine/drive_c/tools_v4.X/Other_Tools/Adobe_ePub_Tools/adeptkey.der)

9. Use ADE running under Wine to dowload all of your purchased ePub ebooks

10. for each book you have downloaded via Adobe Digital Editions
There is no need to use Wine for this step!

'python ineptpub_v5.6.pyw’
this will launch a window with 3 lines
1. key: (allready filled in, otherwise it’s in the path where you did step 8.
2. input file: drmbook.epub
3. output file: name-ypu-want_for_free_book.epub

Also… once you successfully generate your adept.der keyfile using WINE, you can use the regular ineptepub plugin with the standard Linux calibre. Just put the *.der file(s) in your calibre configuration directory.
so if you want you can use calibre in Linux:

11. install the plugins from the tools as discribed in the readmes for win

12. copy the adeptkey.der into the config dir of calibre (~/.config/calibre in debian). Every book imported to calibre will automaticly freed from DRM.

