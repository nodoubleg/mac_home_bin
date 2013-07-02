#!/usr/bin/osascript

-- Usage:
-- $ osacompile -o windowPositions.compiled.scpt windowPositions.scpt
-- $ osascript windowPositions.compiled.scpt --save
-- $ osascript windowPositions.compiled.scpt --restore

-- Change this to be the list of windows you want to save/restore
property affectedProcesses : {"iCal", "iChat", "Textual", "nvALT", "Things"}
property windowRecord : {}

on run argv
	if (count of argv) is equal to 0 then
		log "Please specify one of --save or --restore."
		return
	end if
	
	tell application "System Events"
		if (item 1 of argv is equal to "--save") then
			set windowRecord to {}
			repeat with i from 1 to count affectedProcesses
				set end of windowRecord to {0, {}, {}}
			end repeat
			repeat with p from 1 to count affectedProcesses
				set processName to (item p of affectedProcesses)
				if exists process processName then
					log "Process '" & processName & "' exists"
					tell process processName
						set numWindows to count windows
						set item 1 of item p of windowRecord to numWindows
						repeat with i from 1 to numWindows
							set end of item 2 of item p of windowRecord to position of window i
							set end of item 3 of item p of windowRecord to size of window i
						end repeat
					end tell
				end if
			end repeat
		else
			repeat with p from 1 to count affectedProcesses
				set processName to (item p of affectedProcesses)
				if exists process processName then
					log "Process '" & processName & "' exists"
					tell process processName
						set numWindows to item 1 of item p of windowRecord
						repeat with i from 1 to numWindows
							set position of window i to (item i of item 2 of item p of windowRecord)
							set size of window i to (item i of item 3 of item p of windowRecord)
						end repeat
					end tell
				end if
			end repeat
		end if
	end tell
end run