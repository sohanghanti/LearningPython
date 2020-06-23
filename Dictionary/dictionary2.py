car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

bus = {
  "woo": "PMT",
  "model": "2017",
  "coo": 2008
}
l1 = 1,2,3
l2 = (4,5,6)
l4 = [7,8,9,10,11,12,13,14]

print(l4[:-1])
# l4.insert(2,4)
# print(type(l1))
print(l4)
l3 = l1 + l2
print(l3)


dict3 = {}
list1 = []
for i in car:
    dict3[i] = car[i]

for j in bus:
    if j in dict3:
        list1.append(dict3[j])
        list1.append(bus[j])
        dict3[j] = list1
    else:
        dict3[j] = bus[j]

print(sorted(dict3.items()))   # will return list of tuples in a sorted manner
