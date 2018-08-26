# Make a Desktop cleaner programme that takes all files and moves them into a specific set of folders, based on the extension of the file.

#Ver1
#Run through the whole Desktop
#If the file is a .xml file, put it into a XML folder.
#Do this for all kinds of extensions

#Ver2
#Maybe we can optimize it, so that it takes whatever extension, and creates a folder for that specifically


#Run through the whole desktop

import shutil
import os
import pyperclip

# Ensures that that a document is created, if it doesn't exist.
MainPath = 'C:\\Users\\Klas\\Desktop\\Recycling'
excelpath = 'C:\\Users\\Klas\\Desktop\\Recycling\\Excel' 
wordpath = 'C:\\Users\\Klas\\Desktop\\Recycling\\Word'
Powerpointpath = 'C:\\Users\\Klas\\Desktop\\Recycling\\Powerpoint'
PDFpath = 'C:\\Users\\Klas\\Desktop\\Recycling\\PDF'
XMLpath = 'C:\\Users\\Klas\\Desktop\\Recycling\\XML'
JSONpath = 'C:\\Users\\Klas\\Desktop\\Recycling\\JSON'
TXTpath = 'C:\\Users\\Klas\\Desktop\\Recycling\\TXT'
Picturepath = 'C:\\Users\\Klas\\Desktop\\Recycling\\Picture'
ElsePath = 'C:\\Users\\Klas\\Desktop\\Recycling\\EverythingElse'

#If the folder is not created, create it
if not os.path.exists(MainPath):
    os.makedirs(MainPath)
if not os.path.exists(excelpath):
    os.makedirs(excelpath)
if not os.path.exists(wordpath):
    os.makedirs(wordpath)
if not os.path.exists(Powerpointpath):
    os.makedirs(Powerpointpath)
if not os.path.exists(PDFpath):
    os.makedirs(PDFpath)
if not os.path.exists(XMLpath):
    os.makedirs(XMLpath)
if not os.path.exists(JSONpath):
    os.makedirs(JSONpath)
if not os.path.exists(TXTpath):
    os.makedirs(TXTpath)
if not os.path.exists(Picturepath):
    os.makedirs(Picturepath)
if not os.path.exists(ElsePath):
    os.makedirs(ElsePath)

ExcelExtensions = [".xlsx", ".xls", ".xlsm"]
PictureExtensions = ['.jpeg', '.gif', '.png', 'jpg']

#For loop, run through all files of the given directory and move them according to their file extension (e.g. files with .xlsx are moved to the Excel folder)
for folderName, subfolders, filenames in os.walk('C:\\Users\\Klas\\Desktop\\TestVersion'):
    print('er vi her endnu1?')
    for file in filenames:
        print('er vi her endnu2?')
        if file.endswith(tuple(ExcelExtensions)):
            print('er vi her endnu?3')
            shutil.move((os.path.join(folderName, file)), (excelpath))
            print('1')
        elif file.endswith('.docx'):
            shutil.move((os.path.join(folderName, file)), (wordpath))
            print('2')
        elif file.endswith('.pptx'):
            shutil.move((os.path.join(folderName, file)), (Powerpointpath))
            print('3')
        elif file.endswith('.pdf'):
            shutil.move((os.path.join(folderName, file)), (PDFpath))
            print('4')
        elif file.endswith('.xml'):
            shutil.move((os.path.join(folderName, file)), (XMLpath))
            print('5')
        elif file.endswith('.json'):
            shutil.move((os.path.join(folderName, file)), (JSONpath))
            print('6')
        elif file.endswith('.txt'):
            shutil.move((os.path.join(folderName, file)), (TXTpath))
            print('7')
        elif file.endswith(tuple(PictureExtensions)):
            shutil.move((os.path.join(folderName, file)), (Picturepath))
            print('8')
        else:
            shutil.move((os.path.join(folderName, file)), (ElsePath))
            print('9')