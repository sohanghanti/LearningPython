import copy

l1 = ['cat', 'dog', 'elephant']
l2 = l1


print(l1)
print(l2)

l2[2] = 'pig'

print(l2)
print(l1)

l3 = copy.deepcopy(l1)
l3[2] = 'zebra'
#
print(l3)
print(l1)
print(l2)



