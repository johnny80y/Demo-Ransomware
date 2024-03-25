import os
import time
from PyPDF2 import PdfReader, PdfWriter



def pdf_decryption_function():
    ###########################################################################
    # Get a list of the files in our desired directory:
    ###########################################################################

    # folder path
    dir_path = 'demo-Files'

    files_tmp = [] # new list

    for file in os.listdir(dir_path):
        if '.pdf.demon' in file:
            files_tmp.append(file)

    ###########################################################################
    # Remove the custom File Extension:
    ###########################################################################
    for file in files_tmp:
        old_file = os.path.join("demo-Files", file)
        new_file = os.path.join("demo-Files", file.replace('.demon', ''))
        os.rename(old_file, new_file)

    ###########################################################################
    # Get a list of the files WITHOUT EXTENSIONS in our desired directory:
    ###########################################################################

    # folder path
    dir_path = 'demo-Files'

    files = [] # new list

    for file in os.listdir(dir_path):
        if '.pdf' in file:  # I only want to encrypt .txt-files
            files.append(file)
    print(files) # check --> works


    ###########################################################################
    # Get the decryption Key:
    ###########################################################################
    pdf_crypt_key = "password1234"

    ###########################################################################
    # Open each file and decrypt its contents:
    ###########################################################################

    # Loop through all files:
    for file in files:
        reader = PdfReader(f"demo-Files/{file}")
        writer = PdfWriter()

        if reader.is_encrypted:
            reader.decrypt(pdf_crypt_key)

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Save the new PDF to a file
        with open(f"demo-Files/{file}", "wb") as f:
            writer.write(f)


    ###########################################################################
    # Script Closing Statement:
    ###########################################################################

    print("----------   All files have been decrypted.  ----------")