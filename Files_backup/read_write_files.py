import os


myFile = open('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik\PlainText.txt', 'a+')
myFile.write('My name is Sohan \n')
myFile.close()


myFile = open('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik\PlainText.txt', 'r+')
print(myFile.read())
myFile.close()


myFile = open('C:\pyCharmProjects\Sohan\Suhas\Ghanti\Advik\PlainText.txt', 'r+')
print(myFile.readlines())
myFile.close()


fls = open('PlainText.txt', 'w')
print(os.path.abspath('PlainText.txt'))
fls.write('New text file opened and writing the content')
fls.close()

