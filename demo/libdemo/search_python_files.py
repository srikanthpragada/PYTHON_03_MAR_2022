# Search python files for the given string
# python search_python_files.py search_string [starting_directory]

import os
import sys

def file_has_string(filename, ss):
    with open(filename, "rt") as f:
        return ss in f.read()

# Check whether required params are passed
if len(sys.argv) < 2:
    print("Usage : python search_python_files.py search_string [start_dir]")
    exit(1)

search_string = sys.argv[1]
# if start directory is given
if len(sys.argv) > 2:
    start_dir = sys.argv[2]
else:
    start_dir = os.getcwd() # current dir

entries = os.walk(start_dir)

for (dirname, dirs, files) in entries:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f
            if file_has_string(filename, search_string):
                print(filename)



