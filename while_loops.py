# spam = 0
# while spam < 5:
#     print("hello")
#     spam = spam + 1
#
# ##############################################################
# cnt = 1
# print("Enter the password: ")
# pwd = input()
#
# while pwd != 'Welcome1@3':
#     while cnt != 5:
#         print("Please enter the correct password")
#         pwd = input()
#         cnt = cnt + 1
#         print(cnt)
#     break
#

import json


class Laptop:
    name = 'My Laptop'
    processor = 'Intel Core'


# create object
laptop1 = Laptop()
laptop1.name = str('Dell Alienware')
laptop1.processor = str('Intel Core i7')

# convert to JSON string
jsonStr = json.dumps(laptop1.__dict__)

# print json string
print(type(jsonStr))
