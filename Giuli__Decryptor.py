import os
from cryptography.fernet import Fernet

###########################################################################
# Get a list of the files in our desired directory:
###########################################################################

# folder path
dir_path = 'demo-Files'

files = [] # new list

for file in os.listdir(dir_path):
    if '.txt.meow' in file:
        files.append(file)


###########################################################################
# Get the decryption Key from file:
###########################################################################
# opening the key (reading the content from the file)
with open('demo-Files/filekey.key', 'rb') as filekey:
    key = filekey.read()

#print(key)


###########################################################################
# Open each file and decrypt its contents:
###########################################################################

Decryptor = Fernet(key)

# Loop through all files:
for file in files:
    cryptedFile = open(f'demo-Files/{file}', 'rb') # open file for reading
    encryptedText = cryptedFile.read()
    #encryptedText = bytes(encryptedText, 'utf-8')
    #print("This is the file content:    ", encryptedText)
    decryptedText = Decryptor.decrypt(encryptedText)

    #print(decryptedText)

    rescuedFile = open(f'demo-Files/{file}', 'w') # open file for writing
    rescuedFile.write(bytes.decode(decryptedText))
    rescuedFile.close()


###########################################################################
# Remove the custom File Extension:
###########################################################################
for file in files:
    old_file = os.path.join("demo-Files", file)
    new_file = os.path.join("demo-Files", file.replace('.meow', ''))
    os.rename(old_file, new_file)


###########################################################################
# Delete the Ransom Note & Key File:
###########################################################################
try:
    os.remove("demo-Files/ReadMe.html") # delete Ransom note
    os.remove("demo-Files/filekey.key") # delete key file
except:
    print("Files already removed.")

###########################################################################
# Change Desktop Wallpaper Back to normal:
###########################################################################
#path = "default_tmp.png"
#ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


###########################################################################
# Script Closing Statement:
###########################################################################

print("----------   All files have been decrypted.  ----------")