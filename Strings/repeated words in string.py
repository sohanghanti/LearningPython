str1 = "is country. my All Indians are my brothers and sisters. India sisters. country. India"

repeat = {}
arrStr1 = str1.split(" ")

for i in arrStr1:
    if arrStr1.count(i) > 1:
        repeat[i] = arrStr1.count(i)

print(repeat)

#
# values = []
# for v in repeat.values():
#     values.append(v)
#
# print(values)
#
# maxRepeat = []
# for k, v in repeat.items():
#     if v == max(values):
#         maxRepeat.append(k + " : " + str(v))
#
# print(maxRepeat)
# print("   ".join(sorted(maxRepeat)))






