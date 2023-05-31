import string

# input and output files
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    lines = input_file.readlines()

    for i, line in enumerate(lines, start=1):
        # Loop over the lines
        # counters for each line
        letter_count = 0
        punctuation_count = 0

        # count the letters and punctuation
        for char in line:
            if char.isalpha():
                letter_count += 1
            elif char in string.punctuation:
                punctuation_count += 1

        # output file
        output_file.write(f"Line {i}: {line.strip()} ({letter_count})({punctuation_count})\n")
