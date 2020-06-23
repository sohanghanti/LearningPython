import os
import shutil

folderPath = os.getcwd()

testFolderPath = folderPath + '\\TestFolder'

if os.path.exists(testFolderPath):
    shutil.rmtree(testFolderPath)

os.mkdir(testFolderPath)
os.path.exists(testFolderPath)

testFile = open(testFolderPath + '\\testFile.txt', 'w')
testFile.close()

number = len(os.listdir(folderPath))
print('Total files and folders in ' + folderPath + ': \n' + str(number) + '\n')

print('Files and folders in ' + folderPath + ': ')
for eachFileFolder in os.listdir(folderPath):
    print(eachFileFolder.title())
    if os.path.isdir(eachFileFolder):
        number = len(os.listdir(eachFileFolder))
        if number > 0:
            for eachMember in os.listdir(eachFileFolder):
                print('     ' + eachMember.title())