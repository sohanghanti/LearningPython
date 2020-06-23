str1 = "this is Sohan's house"

str2 = 'this is Sohan\'s house'

str3 = 'hello\nhow are you?\nI am fine'
print(str1[9])
print(str2)
print(str3)

str4 = """my name is Sohan. India is my country.
I stay in Pune. I am working in automation using Python.
Framework design is in progress."""
print(str4)

print(len(str4))

# r in the beginning of the string is for raw string which nullifies the importance
# of the slashes within the string to destroy escape characters coming after slashes
str5 = r'my folder path is C:\windows\myFolder\folder2'

print(str5)

str = 'Hello World'
print(str.index('H'))

print(str.find('x'))
