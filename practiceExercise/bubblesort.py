lst1 = [12, 34, 2, 56, 21, 87, 78]

for i in range(0, len(lst1)):
    for j in range(i+1, len(lst1)):
        if lst1[j] < lst1[i]:
            lst1[j], lst1[i] = lst1[i], lst1[j]
print(lst1)
