# Renamer.py
Renamer.py renames files to my standard.
### File renamer for the following files:
- yyyy-mm-ddThhmmH--[NAME]_File_Name.ext
- yyyy-mm-ddThhmmH--File_Name.ext
- File_Name.ext
- File Name.ext

### Rename with ISO8601 date format:
- File-Name_[NAME]_yyyy-mm-ddThhmmH.ext
- File-Name_yyyy-mm-ddThhmmH.ext

## Notes:
- Renames any files not under the exadox format to become the latter.
- Files with brackets will have brackets placed after the File-Name.
- Files that don't contain brackets will not have brackets.
- Will list down what files will be renamed to.
- Will ask user if the user is going to accept name changes before renaming.

## Based on:
- "https://exadox.com/en/articles/file-naming-convention-ten-rules-best-practice"

<hr>

# RenamerWalk.py
Similar to Renamer.py, but searches for files in subfolders.

<hr>

# RenamerExt.py
RenamerExt.py removes duplicate extension in file name. Seaches subfolders.

### Example:
sample.png.png to sample.png
sample.pngsample.png to samplesample.png

<hr>

# RenamerUnderscore.py
RenamerUnderscore.py removes duplicate underscores. Seaches subfolders.

### Example:
- Sample__.txt to Sample.txt
- Sample__2020-01-01T1000H.txt to Sample_2020-01-01T1000H.txt

<hr>

# RenamerInitHyphen.py
RenamerInitHyphen.py removes initial hyphen of the file. Searches subfolders.

### Example:
- -Sam-ple-.txt to Sam-ple-.txt

<hr>

# RenamerDashTimezone.py
RenamerDashTimezone.py removes dashes and converts my +08:00 timezone code (H) to +0800. For strict ISO-8601 purists. It will only touch filenames with timestamps.

### Example:
- 2023-01-30T1400H to 20230130T1400+0800

<hr>

# Other Stuff
## Renamer.py and RenamerWalk.py
- Removes duplicate underscores (__)
- Removes initial hyphen (r'-')
