str1 = 'the quick brown fox jumps over the lazy dog'

alphabates = 'abcdefghijklmnopqrstuvwxyz'

str1 = [alphabates[alphabates.index(x)+1] if x in alphabates[:-1] else x for x in str1]

print("".join(str1))

# newString = ''
# for x in str1:
#     if x in alphabates[:-1]:
#         newString = newString + (alphabates[alphabates.index(x) + 1])
#     else:
#         newString = newString + x
#
# print(newString)
