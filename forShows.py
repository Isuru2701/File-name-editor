import os
import sys

path = input("enter directory path: ")
name = input("enter name of show: ")

files = ReadDir(name)

def readDir(directory):
    os.chdir(directory)
    files = []

    for file in os.listdir():
        files.append(name + file)
        print(file)
    
    return files
