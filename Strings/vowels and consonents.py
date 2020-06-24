str1 = "python"
v = ''
c = ''
for i in str1:
    if "aeiou".count(i) > 0:
        v = v + " " + i
    else:
        c = c + " " + i


print(v)
print(c)