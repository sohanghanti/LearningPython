import os
import shutil
import pathlib


# COMMENT::::::   run copy_move_files.py before this file   ::::::::::

# remove single file
os.remove(os.getcwd() + '\\movedFile.txt')
print(os.path.exists(os.getcwd() + '\\movedFile.txt'))
# os.unlink(str(os.getcwd()) + '\\movedFile.txt')
pth = pathlib.Path(os.getcwd())
print(pth.parent)

# remove the entire folder with its files inside
shutil.rmtree(str(pth.parent) + '\\Files_backup')
print(os.path.exists(str(pth.parent) + '\\Files_backup'))