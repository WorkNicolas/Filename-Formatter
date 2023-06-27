"""
File renamer for the following files:
- yyyy-mm-ddThhmmH--[NAME]_File_Name.ext
- yyyy-mm-ddThhmmH--File_Name.ext
- File_Name.ext
- File Name.ext

Rename with ISO8601 date format:
- File-Name_[NAME]_yyyy-mm-ddThhmmH.ext
- File-Name_yyyy-mm-ddThhmmH.ext

Notes:
- Renames any files not under the exadox format to become the latter.
- Files with brackets will have brackets placed after the File-Name.
- Files that don't contain brackets will not have brackets.
- Will list down what files will be renamed to.
- Will ask user if the user is going to accept name changes before renaming.

Based on:
- "https://exadox.com/en/articles/file-naming-convention-ten-rules-best-practice"
"""

import os
import re
from datetime import datetime

# determine path to manipulate
path = input("(Renamer.py) Enter Path: ")
os.chdir(path)

# regex patterns
date_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}\d{2}H'
bracket_pattern = r'\[.*?\]'

# only file extensions in this list will be renamed
exts = ['.docx', '.doc', '.odt', '.pptx', '.odp', '.png', '.jpg', '.jfif', '.jpeg', '.gif', '.bmp', '.pdf', '.xlsx', 'xls', '.txt']

# determines if the previous conditional statements were executed
executed = False
queried = False

# ends range(0,2)
changes = False

# loop through all files in current directory
file_size = [file for file in os.listdir(path)]

for i in range(0,2):
    if changes and not queried:
        break
    # compared to file_size
    end = 0
    for filename in os.listdir(path):
        # check if file is not a folder and contains two hyphens
        # checking file extensions is not necessary since I only renamed files on exts
        bracket = ''
        if not os.path.isdir(filename) and '--' in filename:
            # regex file extraction and file extension extraction
            file_ext = os.path.splitext(filename)[1]
            date_match = re.search(date_pattern, filename)
            bracket_match = re.search(bracket_pattern, filename)
            if date_match:
                date = date_match.group()
                try:
                    bracket = bracket_match.group()
                except AttributeError:
                    bracket = ''
                # extract original filename without date and bracket
                orig_filename = re.sub(date_pattern + '|' + bracket_pattern + '|' + file_ext, '', filename).replace('--', '_')
                # remove initial '_'
                orig_filename = orig_filename.replace('_','')
                # replace underscores with hyphens in filename
                new_filename = orig_filename.replace('_', '-')
                # insert date into new filename
                new_filename = f'{new_filename}_{bracket}_{date}{file_ext}'
                # remove '__'
                new_filename = new_filename.replace('__','_')
                # removes '--' in filename
                new_filename = new_filename.replace('--', '')
                # removes initial '-'
                new_filename = re.sub(r'^-', '', filename, count=1)
                # rename file
                if queried:
                    os.rename(filename, new_filename)
                print(f'{filename} to {new_filename}' if not queried else f'Renamed {filename} to {new_filename}')
                executed = True
        # checks if it is not a folder, contains an extension,
        # and does not contain ISO-8601 date
        elif not os.path.isdir(filename) and any(ext in filename for ext in exts) and not re.search(date_pattern, filename):
                # generate ISO-8601 compliant date format
                date_created = os.stat(filename).st_ctime
                date_created_tstamp = datetime.fromtimestamp(date_created)
                date = date_created_tstamp.strftime('%Y-%m-%dT%H%MH')
                # extract file extension
                file_ext = os.path.splitext(filename)[1]
                # replace empty spaces with delimiter
                new_filename = filename.replace(' ', '-')
                # remove extension
                for ext in exts:
                    new_filename = new_filename.replace(ext, '')
                # new file name
                new_filename = f'{new_filename}_{date}{file_ext}'
                # rename file
                if queried:
                    os.rename(filename, new_filename)
                print(f'{filename} to {new_filename}' if not queried else f'Renamed {filename} to {new_filename}')
                executed = True
        elif not executed and end == len(file_size):
            # reached the end of the loop without executing anything
            print("No files were renamed")
            i = 1
        end += 1
    if end == len(file_size) and not queried:
            query = input("Accept Changes [ACCEPT]: ")
            queried = True
            if query.upper() == 'ACCEPT':
                print("Changes accepted")
            else:
                print("Changes not accepted")