import subprocess
import sys

print("""
You are using main.py, here are the following options. Type the number to execute.

[0] Exit

Only target folder
[1] Renamer.py
Rename file with ISO-8601 date format.

Searches for files in subfolders
[2] RenamerDashTimezone.py
Removes dashes from date and replaces timezone code with offset.

[3] RenamerExt.py
Removes duplicate extensions in filenames.

[4] RenamerInitHyphen.py
Removes initial hyphen of the file.

[5] RenamerTimeRemover.py
Removes time from timestamp, leaving only date.

[6] RenamerUnderscore.py
Removes duplicate underscore in filenames.

[7] RenamerWalk.py
Similar to Renamer.py but searches for files in subfolders.
"""
)

usrin = int(input("Input: "))

run_file = None

if usrin == 0:
    exit()
elif usrin == 1:
    run_file = "src/Renamer.py"
elif usrin == 2:
    run_file = "src/RenamerDashTimezone.py"
elif usrin == 3:
    run_file = "src/RenamerInitHyphen.py"
elif usrin == 4:
    run_file = "src/RenamerTimeRemover.py"
elif usrin == 5:
    run_file = "src/RenamerUnderscore.py"
elif usrin == 6:
    run_file = "src/RenamerWalk.py"

print("Running " + run_file)

if run_file :
    subprocess.run([sys.executable, run_file])