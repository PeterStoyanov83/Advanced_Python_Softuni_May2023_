# Reading the numbers from the user and converting them to a list of floats
numbers = list(map(float, input().split()))

# Creating an empty dictionary to store the counts
counts = {}

# Going through each number in the list
for number in numbers:
    # If the number is already in the dictionary, increment its count
    if number in counts:
        counts[number] += 1
    # Otherwise, add the number to the dictionary with a count of 1
    else:
        counts[number] = 1

# Going through each number and its count in the dictionary
for number, count in counts.items():
    # Printing the number and its count, formatted as required
    print(f"{number:.1f} - {count} times")
