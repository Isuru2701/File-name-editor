import os
import shutil
import sys

"""
requirements:
    []reads directory
    []records the names of the files and sub-folders (and their files and folders)
    []saves the names in a text file, comma separated

    []opens file, splits the contents into an array
    []reads directory
    []checks if files and sub-folders match the contents in the file
    []generates report of missing files
    []alerts user

"""

"""
abstract:
    []readDir function
    []loadData function
    []alertUser function
    
"""


class Directory:
    def __init__(self, path):
        self.path = path
        self.contents = os.listdir(os.chdir(path))

    def isEmpty(self):
        if len(self.contents) == 0:
            return True
        else:
            return False


def readDir(directory):
    directory = os.path.normpath(directory)
    os.chdir(directory)
    files = []

    for file in os.listdir():
        files.append(sys.argv[1] + "\\" + file)
        print(file)
    print("------------")
    return files


def loadData(data):
    pass
    # TODO


files = readDir(sys.argv[1])

