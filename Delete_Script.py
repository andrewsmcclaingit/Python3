#!/usr/bin/python3

import os, datetime, time, sys, contextlib

#LogFile -> 'w' overwrite, 'a' append to log
#path -> location of files to be delete (including subfolders)
#currentDate -> getting current date for logging
#olderThanDays -> edit the number after '-', in this case, older than 90 days
#timeNow -> getting current time in seconds
#cnt -> setting counter to 0
#cntCheck -> setting counter to 0
logFile = open('/home/zammad/Documents/logs/DeleteOutput.log','a')
path = '/home/zammad/Documents/Junk/'
currentDate = datetime.datetime.now()
olderThanDays = time.time() - 90 * 86400 #
cnt = 0
cntChk = 0

#Function -> Writing to the log
def writeToLog(input):
	logFile.write(input)
	logFile.write('\n')

#Walking the declared path and counting the number of files older than the set day
for root, dirs, files in os.walk(path):
	for file in files:
		realPath = os.path.join(root, file)
		if os.path.getmtime(realPath) < olderThanDays:
			cnt += 1

#Begin writing to log if files exist
writeToLog(str(currentDate))
writeToLog("----------------------------------")
writeToLog(str(cnt) + " File(s) were found: " )

#Walking the declared path, outputing the filenames older than set day to the log and then deleting them.
#If there is an error deleting the file, suppress the exception
for root, dirs, files in os.walk(path):
	for file in files[:]:
		realPath = os.path.join(root, file)
		if os.path.getmtime(realPath) < olderThanDays:
			writeToLog(os.path.join(root, file))
			with contextlib.suppress(FileNotFoundError):
				os.remove(os.path.join(root, file))

#Check to see if files are actually gone
#Output below
for root, dirs, files in os.walk(path):
	for file in files:
		realPath = os.path.join(root, file)
		if os.path.getmtime(realPath) < olderThanDays:
			cntChk += 1

if cntChk == 0:
	writeToLog("All Files Deleted Successfully")
	writeToLog("----------------------------------")
	writeToLog('\n')
else:
	writeToLog("ERROR: Not All Files Deleted")
	writeToLog("----------------------------------")
	writeToLog('\n')

#Done editing log file, close
logFile.close()
