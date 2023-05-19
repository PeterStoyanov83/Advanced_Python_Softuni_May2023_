# Input string

sublists_str = input().split("|")

# Reverse the order of the sub lists
sublists_str.reverse()

# Flatten the sub lists
flattened = []
for sublist_str in sublists_str:
    # Strip any leading or trailing whitespace from the sublist string
    sublist_str = sublist_str.strip()

    # Split the sublist string into individual numbers, each represented by a string
    numbers_str = sublist_str.split()

    # Convert each number string into an integer and add it to the flattened list
    for number_str in numbers_str:
        flattened.append(int(number_str))

# Print the resulting flattened list, unpacked with *
print(*flattened)
