str1 = "Sohan Suhas Ghanti"

for i in str1:
    if str1.count(i) > 1 and i != " ":
        str1 = str1.replace(i, "")
print(str1)