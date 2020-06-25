str1 = "india is my India country. all Indians are my brothers and sisters"

print('India' in str1)
print('x ' in str1)

print(str1.count(str1[1]))
print(str1.count('India'))
print(str1.index('India'))
print(str1.find('India'))
print(str1.upper())
print(str1.lower())

print(str1.capitalize())

print(str1.isnumeric())
print(str1.isalpha())

str2 = '12345'
print(str2.isnumeric())
print(str2.isalpha())

print(str1.count(' '))

print(str1[::-1])

newStr = ''
for r in range(len(str1)-1, -1, -1):
    newStr = newStr + str1[r]

print(newStr)

print(str1[2])

l2 = str1.split(' ')
print(l2)

print(str1.strip('Indiasisters'))
print(str1.replace('India', 'USA'))
print(str1.startswith('India'))
print(str1.endswith('bangladesh'))
print(str1.rjust(5, '*'))
print(str1.ljust(5, '*'))



