myCat = {'size': 'fat', 'color': 'grey'}


print(type(myCat))
if str(type(myCat)) == "<class 'dict'>":
    print("true")
print(str(type(myCat)) == "<class 'dict'>")

print(myCat.get('size'))
myCat['size'] = 'small'

print(myCat['size'])

print('color' in myCat)

print(myCat.keys())
print(myCat.values())
print(myCat.items())

for k, v in myCat.items():
    print(k, v)

for x in myCat.items():
    print(x)

if 'color' in myCat:
    print(myCat['color'])

print(myCat.get('noise'))

print(len(myCat))
print(myCat.items())
myCat.pop('size')
print(myCat)