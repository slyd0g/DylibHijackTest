import sys
import re
import subprocess

def read_raw_file(path):
    file = open(path, "r")
    for line in file:
        if re.search("HIJACK", line):
            path_clean = line.split("HIJACK_PATH=")[1].strip()
            print("[+]", path_clean, "is hijackable with DYLD_INSERT_LIBRARIES")
            print("[+] Entitlements for", path_clean, "\n")
            sub = subprocess.Popen(["codesign", "-d", "--entitlements", ":-", path_clean])
            sub.wait()
            print("\n\n")

if (len(sys.argv) < 2):
    print("Usage: python3 inspect.py /raw/output/file")
    print("Error: Please enter a path!")
    exit()

read_raw_file(sys.argv[1])