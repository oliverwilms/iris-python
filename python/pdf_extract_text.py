from PyPDF2 import PdfReader

# Open the PDF file
pdfFile = open('visitSummary.pdf', 'rb')

# Create a PdfReader object to read the file
pdfReader = PdfReader(pdfFile)

# Get the number of pages in the PDF
numOfPages = len(pdfReader.pages)

# Loop through all the pages and extract text
for i in range(0, numOfPages):
    print("Page Number: " + str(i))
    print("- - - - - - - - - - - - - - - - - - - -")
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
    print("- - - - - - - - - - - - - - - - - - - -")

# Close the PDF file object
pdfFile.close()
