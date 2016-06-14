#!/usr/bin/env python
#
# This module renames files from fileName.* to YYYYMMDD-HHMMSS-fileName.*

import os
import sys
import re
import PIL.Image

if len(sys.argv) < 3:
    print('\nUsage:\t' + sys.argv[0] + ' pathToFiles' + ' fileExtension\n')
    quit()

filesDir = sys.argv[1]
fileExt = sys.argv[2]
filesList = os.listdir(filesDir)

print('All files found in the directory: ' + filesDir + '\n')
print(filesList)
print('\nWill be processed only ' + fileExt + ' files:\n')

filesExtList = []
for item in filesList:
    matchString = '(.*)' + fileExt
    matchItem = re.match(matchString, item)
    if matchItem:
        filesExtList.append(item)

print(filesExtList)

print('Old file name:\t\tDate taken:\t\tNew file name:\n' + '-'*77)

if fileExt == 'JPG':
    os.chdir(filesDir)
    for fileName in filesExtList:
        fileOpened = PIL.Image.open(fileName, 'r')
        dateTaken = fileOpened._getexif()[36867]
        m1 = re.match('(.*):(.*):(.*)\ (.*):(.*):(.*)', dateTaken)
        dateTaken2 = m1.group(1) + m1.group(2) + m1.group(3) + '-' + m1.group(4) + m1.group(5) + m1.group(6)
        newFileName = dateTaken2 + '-' + fileName 
        print(fileName + '\t\t' + dateTaken + '\t' + newFileName)
        fileOpened.close()
        os.rename(fileName, newFileName)

if fileExt == 'MOV':
    print('MOV renaming not developed yet.')
