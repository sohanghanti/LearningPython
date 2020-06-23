import PyPDF2


writer = PyPDF2.PdfFileWriter()

writer.addBlankPage(200.0, 100)
myPage = writer.getPage(0)

content = 'Sohan Ghanti'
writer.write(content)

newPDFFile = open('newPDF.pdf', 'wb')
writer.write(newPDFFile)

newPDFFile.close()