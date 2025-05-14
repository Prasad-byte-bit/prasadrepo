#!/usr/bin/env python

import os
import subprocess

# Directory to store the output
dir_path = "/tmp/memory_output"

# Create the directory if it doesn't exist (Python 2.7-compatible)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Output file path
file_path = os.path.join(dir_path, "memory_info.txt")

# Run 'free -m' command to get memory info
try:
    memory_info = subprocess.check_output(["free", "-m"])
    
    # Write the output to the file
    with open(file_path, "w") as f:
        f.write(memory_info)
        
    print("Memory information written to:", file_path)

except Exception as e:
    print("Error occurred:", str(e))

