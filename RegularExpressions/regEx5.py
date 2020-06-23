import re

txt = '''Cell: 023-134-12345
resume numbers of candidates wit names and addresses
avc 123-223-1234 abcd 224-245-2345
ok alright done'''
regEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = regEx.findall(txt)
print(mo)

# (r'[aeiouAEIOU]')   : all the vowels in a string
# (r'[^aeiouAEIOU]')  : all the characters which are NOT vowels in a string
# (r'\d\s\w+') : all the patterns with numbers followed by space followed by word at least one or more than once
# (r'\D\S\W+') : all the patterns without "numbers followed by space followed by word at least one or more
# than one time"




