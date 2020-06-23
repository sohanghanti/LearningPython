# list1 = [[4, 1], [3, 2], [6, 3]]
#
# print(sorted(list1))
#
#
# for i, j in sorted(list1):
#     print(j, i)


a = [1, 2, 3]


def square(a):
    for i in range(0, len(a)-1):
        return a[i] ** 2


print(square(a))

