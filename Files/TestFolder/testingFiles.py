f = open(r"C:\Users\ghantsoh\Desktop\testing.txt", "r")
# str1 = f.read()
str1 = f.read()
print(str1)
print("List of Words = ", str1.split())
# lst1 = list(str1.split())

dup = {}
for i in str1.split():
    if str1.split().count(i) > 1:
        dup[i] = str1.split().count(i)
print(dup)

values = []
for v in dup.values():
    values.append(v)

maxValues = []
for k,v in dup.items():
    if v == max(values):
        maxValues.append(k + ":" + str(v))

print(sorted(maxValues))