import csv

csvFile = open('DataSalary.csv', 'r')

csvData = csv.reader(csvFile)
print(type(csvData))
dataList = list(csvData)
print(dataList)

for eachRow in dataList:
    print(eachRow)
    l1 = len(eachRow)
    for d in range(0, l1):
        print(eachRow[d])

