#!/usr/bin/env python
#
# This module renames files from fileName.* to YYYYMMDD-HHMMSS-fileName.*

import os
import sys
import re
import PIL.Image

if len(sys.argv) < 3:
    print('\n\tUsage:\t' + sys.argv[0] + ' pathToFiles' + ' fileExtension\n')
    quit()

filesDir = sys.argv[1]
fileExt = sys.argv[2]
filesList = os.listdir(filesDir)

print('\n\tFull list of the ' + filesDir + ' directory:')
print(filesList)
print('\t(%d total)' % len(filesList))
print('\n\tFiltered to be processed (' + fileExt + ' only):')

filesExtList = []
for item in filesList:
    matchString = '(.*)' + fileExt
    matchItem = re.match(matchString, item)
    if matchItem:
        filesExtList.append(item)
print(filesExtList)
print('\t(%d total)' % len(filesExtList))

print('\nOld file name:\t\tDate taken:\t\tNew file name:\n' + '-'*77)

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
