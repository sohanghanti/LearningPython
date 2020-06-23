import os

print(os.path.basename(os.getcwd()))
print(os.getcwd())
os.chdir("C:\pyCharmProjects\Folders")
print(os.getcwd())

print(os.path.exists("C:\pyCharmProjects\Folders"))
print(os.path.basename((os.getcwd())))

print(os.path.relpath('C:\pyCharmProjects\learningPython\Files', 'C:\pyCharmProjects'))

print(os.path.dirname(r'C:\pyCharmProjects\Folders\Images\New Bitmap Image.bmp'))

print(os.path.basename(r'C:\pyCharmProjects\Folders\Images\New Bitmap Image.bmp'))
print(os.path.isfile(r'C:\pyCharmProjects\Folders\Images\New Bitmap Image.bmp'))
print(os.path.isdir(r'C:\pyCharmProjects\Folders\Images'))

print(os.path.getsize(r'C:\pyCharmProjects\learningPython'))
print(os.listdir(r'C:\pyCharmProjects\learningPython'))

print(os.makedirs('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik'))
print(os.path.isdir('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik'))
print(os.path.isfile('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik'))
os.rmdir('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik')
print(os.path.exists('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik'))

