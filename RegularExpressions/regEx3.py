import re


# ? indicates that a pattern can appear 0 or 1 time in an expression
regEx = re.compile(r'Bat(wo)?man')

mo = regEx.search("The Adventures of Batman")
print(mo.group())

mo = regEx.search("The Adventures of Batwoman")
print(mo.group())

# here the area code in the parenthesis can appear 0 or one time in a phone number,
# hence the number with or without area code in the parenthesis can work
regEx = re.compile(r'(\d\d\d)?(\d\d\d-\d\d\d\d)')
mo = regEx.search('My number is 879-3464')
print(mo.group())
mo = regEx.search('My number is (878)879-3464')
print(mo.group())


# * indicates that a pattern can appear 0 or any number of times
regEx = re.compile(r'Bat(wo)*man')
mo = regEx.search("The Adventures of Batman")
print(mo.group())

mo = regEx.search("The Adventures of Batwoman")
print(mo.group())

mo = regEx.search("The Adventures of Batwowowowowoman")
print(mo.group())


# + indicates that a pattern should appear at least 1 time or more than 1 times
regEx = re.compile(r'Bat(wo)+man')
mo = regEx.search("the Adventures of Batwoman")
print(mo.group())

mo = regEx.search("the Adventures of Batwowoman")
print(mo.group())
