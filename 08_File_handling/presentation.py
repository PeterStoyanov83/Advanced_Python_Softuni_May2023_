file = open("text.txt", "r")
lines = file.readlines()

for index, line in enumerate(lines):
    print(f"Row {index + 1} content: '{line.strip()}' ")

file.close()