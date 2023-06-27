"""_summary_
RenamerInitHyphen.py removes initial hyphen of the file. Searches subfolders.
"""

import os
import re

path = input("(RenamerInitHyphen.py): ")

# only file extensions in this list will be renamed
exts = ['.docx', '.doc', '.odt', '.pptx', '.odp', '.png', '.jpg', '.jfif', '.jpeg', '.gif', '.bmp', '.pdf', '.xlsx', 'xls', '.txt']

# determines if the previous conditional statements were executed
executed = False
queried = False

# ends range(0,2)
changes = False

for i in range(0,2):
    if queried and not changes:
        break
    for root, dirs, files in os.walk(path):
        os.chdir(root)
        end = 0
        for filename in os.listdir(root):
            file_ext = os.path.splitext(filename)[1]
            if re.match(r'^-', filename) and file_ext != '':
                new_filename = re.sub(r'^-', '', filename, count=1)
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