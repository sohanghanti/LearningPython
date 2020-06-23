l1 = ['sohan', 'ghanti', 2, 'advik', 'arati']

print(l1[-1])
print(l1[-2])

# slice evaluates to a new list
print(l1[1:3])

# replace a vlaue in a list
l1[1] = 'marathe'
print(l1)

# assign a list in a new list
l1[1:3] = ['deshmukh', 'new', 'surname', 'taken', 'liked']
print(l1)

print(l1[:3])
print(l1[3:])

del l1[1]
print(l1)

l1.remove('liked')
print(l1)


l1.clear()
print(l1)

del l1
print(l1)



