# Read the number of names from the input
n = int(input())

# Create an empty set to store the unique names
unique_names = set()

# Go through each name
for _ in range(n):
    # Read the name from the input
    name = input()

    # Add the name to the set (this automatically discards duplicates)
    unique_names.add(name)

# Print each unique name
for name in unique_names:
    print(name)
