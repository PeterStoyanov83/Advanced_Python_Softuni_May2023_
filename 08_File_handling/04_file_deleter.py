import os

try:
    os.remove("my_first_file.txt")
    print("File removed")
except FileNotFoundError:
    print("File already removed")
