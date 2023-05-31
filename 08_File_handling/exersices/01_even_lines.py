with open("input.txt", "r") as file:
    lines = file.readlines()

# Loop over the lines, only considering even ones
for i in range(0, len(lines), 2):
    line = lines[i].strip()

    # Replace the specified characters with "@"
    for char in ["-", ",", ".", "!", "?"]:
        line = line.replace(char, "@")

    # Reverse the order of the words and print
    print(' '.join(line.split()[::-1]))
