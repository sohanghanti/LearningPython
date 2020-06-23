lst1 = [1,2,2,3,1,2,1,2,1,2,3,3,3,3,3,4,1,2,1,2,12,3,4,5]


def occur(lst):
    newList = []
    maximum = lst.count(lst[0])
    for i in lst:
        occurrence = lst1.count(i)
        if occurrence == maximum:
            newList.append(i)
        elif occurrence > maximum:
            newList.clear()
            newList.append(i)
            maximum = occurrence
    return list(set(newList))


print(occur(lst1))
