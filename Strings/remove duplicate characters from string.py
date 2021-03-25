str1 = "Sohan Suhas Ghanti"

# for i in str1:
#     if str1.count(i) > 1 and i != " ":
#         str1 = str1.replace(i, "")
# print(str1)


list1 = []
for i in str1:
    if i != " ":
        if list1.count(i) == 0:
            list1.append(i)
    else:
        list1.append(i)

print("".join(list1))

