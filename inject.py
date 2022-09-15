import subprocess
import os
import sys
from macholib import MachO

## https://stackoverflow.com/questions/56960818/how-to-check-whether-a-file-is-a-macos-executable-from-python
def read_macho_headers( file ):
    try:
        return MachO.MachO( file ).headers
    except Exception:                   # not a Mach-O file
        return None

## https://stackoverflow.com/questions/19587118/iterating-through-directories-with-python
def walk_directories_execute( root_directory, dylib_path ):
    for subdir, dirs, files in os.walk(root_directory):
        for file in files:
            current_file = os.path.join(subdir, file)
            macho_headers = read_macho_headers(current_file)
            if macho_headers != None:
                if macho_headers[0].header.filetype == 2: ## MH_EXECUTE
                    my_env = os.environ.copy()
                    my_env["DYLD_INSERT_LIBRARIES"] = dylib_path
                    try:
                        subprocess.Popen(current_file, env=my_env)
                    except:
                        pass
            
if (len(sys.argv) < 2):
    print("Usage: python3 inject.py /path/to/recurse /path/to/dylib/to/inject > output.txt")
    print("Error: Please enter a path!")
    exit()

walk_directories_execute(sys.argv[1], sys.argv[2])

