list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

newList = []
for i in range(0, len(list1)):
        newList.append(list1[i] + list2[i])

print(newList)

# print(list1.append(list2))