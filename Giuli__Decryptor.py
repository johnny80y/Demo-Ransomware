import os
from cryptography.fernet import Fernet

###########################################################################
# Get a list of the files in our desired directory:
###########################################################################

# folder path
dir_path = 'C:\\Users\\Administrator\\Documents'

files = [] # new list

for file in os.listdir(dir_path):
    if '.txt' in file:
        files.append(file)


###########################################################################
# Get the decryption Key from file:
###########################################################################
# opening the key (reading the content from the file)
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

print(key)


###########################################################################
# Open each file and decrypt its contents:
###########################################################################

Decryptor = Fernet(key)

# Loop through all files:
for file in files:
    cryptedFile = open(f'C:\\Users\\Administrator\\Documents\\{file}', 'rb') # open file for reading
    encryptedText = cryptedFile.read()
    #encryptedText = bytes(encryptedText, 'utf-8')
    print("This is the file content:    ", encryptedText)
    decryptedText = Decryptor.decrypt(encryptedText)

    print(decryptedText)

    rescuedFile = open(f'C:\\Users\\Administrator\\Documents\\{file}', 'w') # open file for writing
    rescuedFile.write(bytes.decode(decryptedText))
    rescuedFile.close()




