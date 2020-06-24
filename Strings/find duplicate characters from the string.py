str1 = "Sohan Suhas Ghanti"

dup = []
for i in str1:
    str1 = str1.replace(" ", "")
    if str1.count(i) > 1:
        if dup.count(i) == 0:
            dup.append(i)


print(dup)

