import tabula

# Specify the path to the PDF file
pdf_file_path = "/Users/amarmohite/Downloads/test1.pdf"

# Specify the page number(s) of the PDF file that contain the table(s) you want to extract
pages = "all"

# Convert the PDF file to a CSV file using tabula-py
tabula.convert_into(pdf_file_path, "/Users/amarmohite/Downloads/output.csv", output_format="csv", pages=pages)
