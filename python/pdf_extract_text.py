from PyPDF2 import PdfFileReader

# Open the PDF file
pdfFile = open('visitSummary.pdf', 'rb')

# Create a PdfFileReader object to read the file
pdfReader = PdfFileReader(pdfFile)

# Print document information
print("PDF File name: " + str(pdfReader.getDocumentInfo().title))
print("PDF File created by: " + str(pdfReader.getDocumentInfo().creator))
print("- - - - - - - - - - - - - - - - - - - -")

# Get the number of pages in the PDF
numOfPages = pdfReader.getNumPages()

# Loop through all the pages and extract text
for i in range(0, numOfPages):
    print("Page Number: " + str(i))
    print("- - - - - - - - - - - - - - - - - - - -")
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
    print("- - - - - - - - - - - - - - - - - - - -")

# Close the PDF file object
pdfFile.close()
