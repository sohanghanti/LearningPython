sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}

newDict = {}
for k in sampleDict.keys():
    if k == 'name' or k == 'salary':
        newDict[k] = sampleDict[k]

print(newDict)