import os
import time
from PyPDF2 import PdfReader, PdfWriter
# https://pypdf2.readthedocs.io/en/3.0.0/user/encryption-decryption.html
# https://hackernoon.com/how-to-encrypt-a-pdf-using-python

def pdf_encryption_function():
    ###########################################################################
    # Get a list of the PDF-files in our desired directory:
    ###########################################################################

    # folder path
    dir_path = 'demo-Files'

    files = [] # new list

    for file in os.listdir(dir_path):
        if '.pdf' in file:  # I only want to encrypt .txt-files
            files.append(file)
    print(files) # check --> works



    ###########################################################################
    # Encrypt PDF
    ###########################################################################
    # Encryption Key:
    pdf_crypt_key = "password1234"

    for file in files:
        reader = PdfReader(f"demo-Files/{file}")
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(pdf_crypt_key)
        # Save encrypted file:
        with open(f"demo-Files/{file}", "wb") as f:
            writer.write(f)
        time.sleep(1)

    ###########################################################################
    # Add a custom Extension to all files:
    ###########################################################################

    # Add Custom extension:
    for file in files:
        old_file = os.path.join("demo-Files", file)
        new_file = os.path.join("demo-Files", "{filename}.demon".format(filename = file))
        os.rename(old_file, new_file)
        time.sleep(1) # sleep for 1 second




    print("----------   All PDF-Files Have Been Encrypted.  ----------")
