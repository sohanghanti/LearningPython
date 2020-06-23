import random
import sys
import pyperclip

print(random.randint(100000000000000000, 999999999999999999)) # last value is included
print(random.randrange(100000000000000000, 999999999999999999))   # last value is not included
print(random.random())

# pyperclip is the thrid prty module has copy and paste functions to read and write on the keyboard
pyperclip.copy("Sohan Ghanti")
pyperclip.paste()

sys.exit()



