list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# for x in list1:
#     if x == "":
#         list1.remove(x)
# print(list1)

list1 = [x for x in list1 if x != ""]

print(list1)