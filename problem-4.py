# Write a python program to print the contents of a directory using the os module. Search online for the function which does that 

import os

# Specify the directory path (use '.' for the current directory)
directory_path ='.'  # Current directory

# Get the contents of the directory
directory_contents = os.listdir(directory_path)

# Print the contents
for item in directory_contents:
    print(item)
