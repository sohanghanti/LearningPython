lst1 = [1, 2, 2, 3, 1, 2, 1, 2, 1, 2, 3, 3, 3, 3, 3, 4, 1, 2, 1, 2, 12, 3, 4, 5]

# def occur(lst):
#     newList = []
#     maximum = lst.count(lst[0])
#     for i in lst:
#         occurrence = lst1.count(i)
#         if occurrence == maximum:
#             newList.append(i)
#         elif occurrence > maximum:
#             newList.clear()
#             newList.append(i)
#             maximum = occurrence
#     return list(set(newList))
#
#
# print(occur(lst1))

max = lst1.count(lst1[0])
maxOccurred = {}

for i in lst1:
    if lst1.count(i) == max:
        maxOccurred[i] = max
    elif lst1.count(i) > max:
        max = lst1.count(i)
        maxOccurred.clear()
        maxOccurred[i] = max

print(maxOccurred)
