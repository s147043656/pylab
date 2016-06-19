#!/usr/bin/env python
#
# This module is developed for renaming of JPG and  MOV  media files from 
# fileName.* to YYYYMMDD-HHMMSS-fileName.* using EXIF "Date taken" property

import sys
import os
import datetime
import re
import PIL.Image

if len(sys.argv) < 3:
    print('\n\tUsage:\t' + sys.argv[0] + ' pathToFiles' + ' fileExtension\n')
    sys.exit(1)

filesDir = sys.argv[1]
fileExt = sys.argv[2]
filesList = os.listdir(filesDir)
print('\n\t### Full list of the ' + filesDir + ' directory:\n%s' % filesList)
print('\t(%d total)' % len(filesList))

filesExtList = []
for item in filesList:
    matchString = '(.*)' + fileExt
    matchItem = re.match(matchString, item)
    if matchItem:
        filesExtList.append(item)
print('\n\t### Filtered to be processed (' + fileExt + ' only):\n%s' % filesExtList)
print('\t(%d total)' % len(filesExtList))

print('\n\t### Processing:\nOld file name\t\tDate taken\t\tNew file name\n' + '-'*77)
if fileExt == 'JPG'or fileExt == 'jpg':
    os.chdir(filesDir)
    processedFiles = 0
    for fileName in filesExtList:
        fileOpened = PIL.Image.open(fileName, 'r')
        dateTaken = fileOpened._getexif()[36867]
        fileOpened.close()
        m1 = re.match('(.*):(.*):(.*)\ (.*):(.*):(.*)', dateTaken)
        dateTaken2 = m1.group(1) + m1.group(2) + m1.group(3) + '-' + m1.group(4) + m1.group(5) + m1.group(6)
        m2 = re.match(dateTaken2, fileName)
        if not m2:
            newFileName = dateTaken2 + '-' + fileName 
            print(fileName + '\t\t' + dateTaken + '\t' + newFileName)
            fileOpened.close()
            os.rename(fileName, newFileName)
            processedFiles +=1 
    print('\t(Total processed: %d)' % processedFiles)

if fileExt == 'MOV' or fileExt == 'mp4':
    os.chdir(filesDir)
    processedFiles = 0
    for fileName in filesExtList:
        fileStat = os.stat(fileName)
        dateTaken = str(datetime.datetime.fromtimestamp(fileStat.st_mtime))
        m1 = re.match('(.*)-(.*)-(.*)\ (.*):(.*):(.*)', dateTaken)
        dateTaken2 = m1.group(1) + m1.group(2) + m1.group(3) + '-' + m1.group(4) + m1.group(5) + m1.group(6)
        m2 = re.match(dateTaken2, fileName)
        if not m2:
            newFileName = dateTaken2 + '-' + fileName 
            print(fileName + '\t\t' + dateTaken + '\t' + newFileName)
            os.rename(fileName, newFileName)
            processedFiles +=1 
    print('\t(Total processed: %d)' % processedFiles)
