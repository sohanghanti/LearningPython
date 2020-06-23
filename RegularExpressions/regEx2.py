import re


regEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = regEx.search('My number is 878-879-3464')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))

regEx = re.compile(r'(\(\d\d\)) (\d\d\d-\d\d\d-\d\d\d\d)')
mo = regEx.search('my number is (91) 878-879-3464')
print(mo.group(1))
print(mo.group(2))
print(mo.group())