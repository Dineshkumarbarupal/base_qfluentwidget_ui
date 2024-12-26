import PyPDF2

def pdf_to_text(pdf_path, output_text_file):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(pdf_file)
        # Open the output text file in write mode
        with open(output_text_file, 'w', encoding='utf-8') as text_file:
            # Loop through all the pages in the PDF
            for page in reader.pages:
                # Extract text from the current page
                text = page.extract_text()
                # Write the extracted text to the output file
                if text:  # Avoid writing empty pages
                    text_file.write(text + '\n')
                    
# Example usage
pdf_to_text("PLAN A.pdf", "output.txt")
