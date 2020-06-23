import re

regEx = re.compile(r'^Hello')   # the entire text begins with Hello
mo = regEx.search('Hello Sir!')
print(mo.group())

# the entire text ends with goodbye
regEx = re.compile(r'goodbye$')
mo = regEx.search('Hello Sir!  Ok goodbye')
print(mo.group())


# Dot (.) character: any character  e.g.  '.at' means any single character before 'at'  like cat, fat, mat, bat sat etc.
# '.{1,2}at' means any character at lease one or max 2 times before 'at', like, flat, (space)cat, (space)bat, brat etc.


