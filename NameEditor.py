"""
abstract
    [] read files in given directory.
    [] look for the pattern '_-_n' in filename, where n is the episode number, if n <10, it should be in 0n form.
    []renames file name to '<name> ep<n> where name and n are given.
"""

import os
import pdb

pdb.set_trace()

path = input("enter directory path: ")
name = input("enter name of show: ")

os.chdir(path)
files = list(os.listdir())
print(files)

for i in range(1, len(files) + 1):
    if i < 10:
        snip = f"_-_0{i}"
    else:
        snip = f"_-_{i}"

    for file in files:
        if snip in file:
            new_name = fr"{path}\{name} ep{i}.mp4"
            print(new_name)
            os.rename(file, new_name)

