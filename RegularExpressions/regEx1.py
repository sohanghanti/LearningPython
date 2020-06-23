import re

# ? indicates, the pattern can apear 0 or 1 time in an expression
batRegEx = re.compile(r'Bat(wo)*man')
mo = batRegEx.search('The adventures of Batman')
print(mo.group())
mo = batRegEx.search('The adventures of Batwoman')
print(mo.group())
mo = batRegEx.search('The adventures of Batwowowowoman')
print(mo.group())


#########################################

#  re.compile will create reg ex object
phoneRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#  .search method will find the first occurrence of the matching pattern
mo = phoneRegEx.search('My number is 838-082-2122')
print(mo.group())

# findall method will find all the occurrences and return the list
mo = phoneRegEx.findall('My number is 838-082-2122 or call me at 878-879-3464')
print(mo)


