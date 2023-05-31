# Create and write to 'words.txt'
with open("words.txt", "w") as word_count_file:
    word_count_file.write("quick is fault")

# Create and write to 'input.txt'
with open("input.txt", "w") as input_file:
    input_file.write(
        """-I was quick to judge him, but it wasn't
his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here…It is safer."""
    )

# Read from 'words.txt'
with open("words.txt", "r") as word_count_file:
    words_to_count = word_count_file.read().lower().split()

# Read from 'input.txt'
with open("input.txt", "r") as input_file:
    text = input_file.read().lower()

# Create a dictionary to store the frequency of each word
word_frequencies = {word: text.split().count(word) for word in words_to_count}

# Sort the words by frequency in descending order
sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

# Write the results to 'output.txt'
with open("output.txt", "w") as output_file:
    for word, frequency in sorted_word_frequencies:
        output_file.write(f"{word}: {frequency}\n")
