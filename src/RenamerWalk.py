"""_summary_
Similar to Renamer.py, but searches for files in subfolders.
"""

import os
import re
from datetime import datetime

# determine path to manipulate
path = input("(RenamerWalk.py) Enter Path: ")

# gets list of files
file_list = []
for root, dirs, files in os.walk(path):
    file_list += files

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
    
for i in range(0,2):
    if queried and not changes:
        break
    for root, dirs, files in os.walk(path):
        os.chdir(root)
        end = 0
        for filename in os.listdir(root):
            bracket = ''
            files_renamed = []
            if not os.path.isdir(filename) and '--' in filename:
                # filename and file ext extraction
                file_ext = os.path.splitext(filename)[1]
                date_match = re.search(date_pattern, filename)
                bracket_match = re.search(bracket_pattern, filename)
                if date_match:
                    date = date_match.group()
                    try:
                        bracket = bracket_match.group()
                    except AttributeError:
                        bracket = ''
                    # extract original filename w/o date and bracket
                    # replace '--' with '_'
                    orig_filename = re.sub(date_pattern + '|' + bracket_pattern + '|' + file_ext, '', filename).replace('--', '_')
                    # remove initial '_'
                    orig_filename = orig_filename.replace('_','')
                    # replace '_' with '-'
                    new_filename = orig_filename.replace('_', '-')
                    # date inserter
                    new_filename = f'{new_filename}_{bracket}_{date}{file_ext}'
                    # remove '__'
                    new_filename = new_filename.replace('__','_')
                    # remove '--'
                    new_filename = new_filename.replace('--', '')
                    # removes initial '-'
                    new_filename = re.sub(r'^-', '', filename, count=1)
                    # rename file
                    if queried:
                        os.rename(filename, new_filename)
                    print(f'{filename} to {new_filename}' if not queried else f'Renamed {filename} to {new_filename}')
                    files_renamed.append(new_filename)
                    executed = True
            # does not contain ISO-8601 date
            elif not os.path.isdir(filename) and any(ext in filename for ext in exts) and not re.search(date_pattern, filename):
                # generate ISO-8601 date
                date_created = os.stat(filename).st_ctime
                date_created_tstamp = datetime.fromtimestamp(date_created)
                date = date_created_tstamp.strftime('%Y-%m-%dT%H%MH')
                # extract file ext
                file_ext = os.path.splitext(filename)[1]
                # replace '' with '-'
                new_filename = filename.replace(' ', '-')
                # remove ext
                for ext in exts:
                    new_filename = new_filename.replace(ext, '')
                # new file name
                new_filename = f'{new_filename}_{date}{file_ext}'
                # rename file
                if queried:
                    os.rename(filename, new_filename)
                print(f'{filename} to {new_filename}' if not queried else f'Renamed {filename} to {new_filename}')
                files_renamed.append(new_filename)
                executed = True
            elif not executed and end == len(file_list):
                # reached the end of the loop without doing anything
                print("No files were renamed")
                i = 1
            end += 1
        print("Root: ", root)
        print("Dirs: ", dirs)
        print("Files: ", files)
        print("Renamed: ", files_renamed)
        print()
    if not queried:
        # execute os.rename
        query = input("Accept Changes [ACCEPT]: ")
        queried = True
        if query.upper() == 'ACCEPT':
            print("Changes accepted")
        else:
            print("Changes not accepted")
            changes = False
                
    