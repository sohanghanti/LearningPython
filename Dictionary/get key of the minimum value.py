sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
#
# lst1 = []
# for v in sampleDict.values():
#   lst1.append(v)
#
# for k in sampleDict.keys():
#   if sampleDict[k] == min(lst1):
#     print(k)


# print("".join([k for k, v in sampleDict.items() if v == min([v for v in sampleDict.values()])]))


print(''.join([k for k, v in sampleDict.items() if v == min([v for v in sampleDict.values()])]))

