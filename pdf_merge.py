import PyPDF2

# Create a PDF merger object
merger = PyPDF2.PdfMerger()

# Add the PDF files to the merger object
merger.append('1 OOPJ.pdf')
merger.append('jvm.pdf')
merger.append('4 scanner.pdf')
merger.append('6 class and object.pdf')
merger.append('3 Control Structure in Java.pdf')
merger.append('7 constructor.pdf')
merger.append('8 Inheritance.pdf')
merger.append('String - Questions.pdf')
merger.append('9 Abstract class (1).pdf')
merger.append('10 Interfaces.pdf')
merger.append('11 Exception handling (1).pdf')

# Write the merged PDF to a new file
merger.write('Java_Total.pdf')
