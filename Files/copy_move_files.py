import shutil
import os

pth = os.getcwd()
print(pth)
print(os.path.basename(pth))
myFilePath = str(pth) + '\\' + 'PlainText.txt'

myFile = open(myFilePath, 'r')
print(myFile.read())

# copy file to another path
if not os.path.exists(pth + '\\copiedFiles'):
    os.mkdir(pth + '\\CopiedFiles')
copiedPath = str(pth) + '\\copiedFiles'
print(copiedPath)
shutil.copy(myFilePath, copiedPath + '\\' + 'copiedFile.txt')
openCopiedFile = open(copiedPath + '\\' + 'copiedFile.txt', 'r')
print(openCopiedFile.read())
openCopiedFile.close()

# copy the folder to another path
if os.path.exists('..\\Files_backup'):
    shutil.rmtree('..\\Files_backup')
shutil.copytree(str(pth), '..\\Files_backup')

print(os.path.exists('..\\Files_backup'))

# cut/paste or move file
shutil.move(copiedPath + '\\' + 'copiedFile.txt', str(pth) + '\\movedFile.txt')
os.path.exists(str(pth) + '\\movedFile.txt')



