import csv

csvFile = open('csvFileWriting.csv', 'w', newline='')

csv_v = csv.writer(csvFile)
csv_v.writerow([1, 2, 3])

csvFile.close()
