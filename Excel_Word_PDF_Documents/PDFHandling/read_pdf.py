import PyPDF2

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

myPage = reader.getPage(10)
print(myPage.extractText())

for pagNum in range(1, reader.numPages):
    print(reader.getPage(pagNum).extractText())

