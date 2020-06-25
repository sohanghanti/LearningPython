emp = ['kelly', 'emma', 'john']
default = {'designation': "developer", 'salary': 8000}

resDict = dict.fromkeys(emp, default)
print(resDict)

print(resDict['kelly'])