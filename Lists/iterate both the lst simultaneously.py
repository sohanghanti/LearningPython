list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

print(list(zip(list1, list2[::-1])))

for i in list(zip(list1, list2[::-1])):
    print(i)
