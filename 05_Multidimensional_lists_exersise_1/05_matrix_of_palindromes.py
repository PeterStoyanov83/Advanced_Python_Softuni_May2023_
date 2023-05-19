# Read the input
rows, cols = map(int, input().split())

# Initialize matrix
matrix = []

# Fill the matrix
for i in range(rows):
    row = []
    for j in range(cols):
        palindrome = chr(97 + i) + chr(97 + i + j) + chr(97 + i)
        row.append(palindrome)
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(' '.join(row))

