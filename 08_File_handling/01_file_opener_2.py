import os

path_to_root = os.path.dirname(os.path.abspath(__file__))

filepath = os.path.join(path_to_root, "text.txt")

if os.path.isfile(filepath):
    print("File found")
else:
    print("File not found")

