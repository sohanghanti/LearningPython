list1 = [72, 26, 79, 70, 20, 68, 43, -71, 71, -2]

list1 = [x * 2 if x%2 == 0 else x-2*x for x in list1]
print(list1)