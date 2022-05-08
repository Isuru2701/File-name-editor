import os
path = input("enter path: ")
os.chdir(path)
print(os.listdir())