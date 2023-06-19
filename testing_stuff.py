import os

# this works:
# os.rename("demo-Files/test_file.txt", "demo-Files/test_file.txt.test")

dir_path = 'demo-Files'

files = [] # new list

for file in os.listdir(dir_path):
    if '.txt' in file:  # I only want to encrypt .txt-files
        files.append(file)

for file in files:
    old_file = os.path.join("demo-Files", file)
    new_file = os.path.join("demo-Files", "{filename}.meow".format(filename = file))
    os.rename(old_file, new_file)
    #os.rename(file, "{filename}.meow".format(filename = file))