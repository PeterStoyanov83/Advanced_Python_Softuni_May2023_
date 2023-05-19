# Read the input
rows, cols = map(int, input().split())
snake = input()

# Initialize the matrix
matrix = []

# Initialize a variable to keep track of the current character in the snake
index = 0

# Fill the matrix
for i in range(rows):
    # Initialize the current row
    row = [''] * cols
    for j in range(cols):
        # Add the current character to the row
        row[j] = snake[index]
        # Move to the next character in the snake, looping back to the start if necessary
        index = (index + 1) % len(snake)
    # If the row number is odd, reverse the row to get the zigzag pattern
    if i % 2 == 1:
        row = row[::-1]
    # Add the row to the matrix
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(''.join(row))
