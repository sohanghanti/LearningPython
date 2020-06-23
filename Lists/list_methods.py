l1 = ['hi', 'hello', 'howdy', 'heyas', 'hi']

print(l1.index('hi'))

print('hi' in l1)

# append method
l1.append('cat')
print(l1)

# insert method
l1.insert(1, 'chicken')
print(l1)

# remove and delete
# remove when you do not know the index of a member in a list
# del when you know the index of a member in a list
l1.remove('chicken')
print(l1)

del l1[3]
print(l1)

print(l1.count('cat'))

l1.append(2)
print(l1)

l1.append((1,2,3,4))
print(l1)


l2 = l1.copy()
print(l2)
l3 = l1

print(l3)
l1[2] = 'man'
print(l1)
print(l3)

l1.pop(2)
print(l1)

l1.clear()

print(l1)
print(l3)
print(l2)


def changeMe(anyList):
    # This changes a passed list into this function
    anyList.append([1, 2, 3, 4])
    print(anyList)
    return


myList = [10, 20, 30]
changeMe(myList)

str1 = 's oan'
print(str1.split())
