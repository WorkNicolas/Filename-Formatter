"""_summary_
RenamerExt.py removes extensions in filename (before the file extension itself). Seaches subfolders.

Example:
- sample.png.png to sample.png
- sample.pngsample.png to samplesample.png
"""

import os
import re

# determine path to manipulate
path = input("(RenamerExt.py) Enter Path: ")

# gets list of files
file_list = []
for root, dirs, files in os.walk(path):
    file_list += files
    
# regex patterns

# only file extensions in this list will be renamed
exts = ['.docx', '.doc', '.odt', '.pptx', '.odp', '.png', '.jpg', '.jfif', '.jpeg', '.gif', '.bmp', '.pdf', '.xlsx', 'xls', '.txt']

# determines if the previous conditional statements were executed
queried = False
changes = False

for i in range(0,2):
    if queried and not changes:
        break
    for root, dirs, files in os.walk(path):
        os.chdir(root)
        end = 0
        for filename in os.listdir(root):
            file_ext = os.path.splitext(filename)[1]
            if file_ext in os.path.splitext(filename)[0] and file_ext != '':
                new_filename = filename.replace(file_ext, '')
                new_filename = f'{new_filename}{file_ext}'
                if queried:
                    os.rename(filename, new_filename)
                print(filename + " to " + new_filename)
    if not queried:
        query = input("Accept Changes [ACCEPT]: ")
        queried = True
        if query.upper() == 'ACCEPT':
            print("Changes accepted")
            changes = True
        else:
            print("Changes not accepted")
            changes = False
            