import re

# specific number of repetition of a group
# the string "Ha" should appear exactly 3 times in an string
regEx = re.compile(r'(Ha){3}')
mo = regEx.search('He said "HaHaHa"')
print(mo.group())


# if we want to match multiple phone numbers that may or may not have the area code
regEx = re.compile(r'(((\d\d\d-)?\d\d\d-\d\d\d\d)(,)?){3}')
mo = regEx.search('my numbers are (878)-879-3464,879-3464,879-879-3464')
print(mo.group())


# range of possible repetitions
regEx = re.compile(r'(Ha){3,5}')
mo = regEx.search('He said "HaHaHaHa"')
print(mo.group())