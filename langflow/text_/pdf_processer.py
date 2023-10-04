# Building a function that loads the text of all pdf files in a directory into a text file

import os
import PyPDF2

def pdf_to_text(path):
    """
    Function that takes a path to a directory and returns a text file with all the pdf files in the directory
    :param path: path to directory
    :return: text file with all the pdf files in the directory
    """
    # Create a list of all the files in the directory
    files = os.listdir(path)
    # Create a text file
    os.chdir('/Users/tamasmakos/dev/langflow/text_/pdfs/Output')
    with open('pdf_text.txt', 'w') as f:
        # Loop through all the files in the directory
        for file in files:
            # Check if the file is a pdf file
            if file.endswith('.pdf'):
                # Open the pdf file
                pdf_file = open(path + file, 'rb')
                # Create a pdf reader object
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                # Loop through all the pages of the pdf
                for page_num in range(len(pdf_reader.pages)):
                    # Get the page object
                    page = pdf_reader.pages[page_num]
                    # Extract the text from the page
                    text = page.extract_text()
                    # Write the text to the text file
                    f.write(text)
                # Close the pdf file
                pdf_file.close()
    # Return the path to the text file
    return os.getcwd() + '/pdf_text.txt'

# Test the function
print(pdf_to_text('/Users/tamasmakos/dev/langflow/text_/pdfs/Input/'))

