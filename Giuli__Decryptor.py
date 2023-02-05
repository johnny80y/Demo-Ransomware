import os
from cryptography.fernet import Fernet

###########################################################################
# Get a list of the files in our desired directory:
###########################################################################

# folder path
dir_path = '/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files'

files = [] # new list

for file in os.listdir(dir_path):
    if '.txt' in file:
        files.append(file)


###########################################################################
# Get the decryption Key from file:
###########################################################################
# opening the key (reading the content from the file)
with open('/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files/filekey.key', 'rb') as filekey:
    key = filekey.read()

print(key)


###########################################################################
# Open each file and decrypt its contents:
###########################################################################

Decryptor = Fernet(key)

# Loop through all files:
for file in files:
    cryptedFile = open(f'/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files/{file}', 'rb') # open file for reading
    encryptedText = cryptedFile.read()
    #encryptedText = bytes(encryptedText, 'utf-8')
    print("This is the file content:    ", encryptedText)
    decryptedText = Decryptor.decrypt(encryptedText)

    print(decryptedText)

    rescuedFile = open(f'/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files/{file}', 'w') # open file for writing
    rescuedFile.write(bytes.decode(decryptedText))
    rescuedFile.close()




