circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas))

print(result)


def rounding(x):
    round(x)


print(list(map(rounding, circle_areas)))


list1 = [2, 1, 3, 0, 5, 4]
for i in range(0, len(list1)-1):
    for j in range(0, len(list1)):
        if list1[i] + list1[j] == 5:
            print(list1[i], list1[j])


first = (1, 2, 3)
second = 'any', 'thing', first

print(second)
