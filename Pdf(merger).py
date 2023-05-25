import PyPDF2

def add_page_multiple_times(src_pdf_path, dest_pdf_path, page_num, num_copies, insert_locations):
    with open(src_pdf_path, 'rb') as src_file, open(dest_pdf_path, 'wb') as dest_file:
        src_pdf = PyPDF2.PdfReader(src_file)
        dest_pdf = PyPDF2.PdfWriter()

        # Get the page to be inserted
        page_to_insert = src_pdf.pages(page_num - 1)

        # Insert the page multiple times at specified locations
        for location in insert_locations:
            dest_pdf.insertPage(page_to_insert, location - 1)

        # Add the remaining pages from the source PDF to the destination PDF
        num_pages = src_pdf.getNumPages()
        for i in range(num_pages):
            if i != (page_num - 1):
                dest_pdf.addPage(src_pdf.getPage(i))

        # Save the modified destination PDF to a file
        dest_pdf.write(dest_file)

# Usage example
source_pdf_path = '/Users/amarmohite/Desktop/CBBG/Stipend/last page.pdf'  # Path to the source PDF file
destination_pdf_path = '/Users/amarmohite/Desktop/CBBG/Stipend/Participant form 2nd Stipend/Final_part 1_removed_removed (1).pdf'  # Path to the destination PDF file
page_number = 1  # Page number to be inserted (starting from 1)
copies = 1  # Number of copies of the page to be inserted
insert_locations = [2]  # Insertion locations in the destination PDF

add_page_multiple_times(source_pdf_path, destination_pdf_path, page_number, copies, insert_locations)
