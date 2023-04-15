"""_summary_
RenamerUnderscore.py removes duplicate underscores. Seaches subfolders.

Example:
- Sample__.txt to Sample.txt
- Sample__2020-01-01T1000H.txt to Sample_2020-01-01T1000H.txt
"""

import os

# determine path to manipulate
path = input("(RenamerUnderscore.py) Enter Path: ")

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
            if '__' in filename:
                new_filename = filename.replace('__', '_')
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