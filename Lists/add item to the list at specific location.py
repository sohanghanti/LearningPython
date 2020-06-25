list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]


# add 7000 after 6000


def findNode(anyList, anyValue):
    for i in anyList:
        if str(type(i)).find('list') > 0:
            findNode(i, anyValue)
        else:
            if i == anyValue:
                anyList.append(7000)


findNode(list1, 6000)
print(list1)



