str1 = 'amry'

str2 = 'mary'

tmp = False
for i in str1:
    if str1.count(i) == str2.count(i) and len(str1) == len(str2):
        tmp = True

if tmp:
    print('anagrams')