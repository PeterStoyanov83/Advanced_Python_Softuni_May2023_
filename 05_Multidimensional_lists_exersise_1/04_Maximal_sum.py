# Read the input
rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

# Initialize max sum
max_sum = float('-inf')

# Initialize the starting position for the 3x3 matrix with max sum
max_row = max_col = 0

# Iterate over the matrix, checking each 3x3 square
for i in range(rows - 2):
    for j in range(cols - 2):
        # Calculate the sum of the current 3x3 square
        current_sum = sum(matrix[i][j:j + 3] + matrix[i + 1][j:j + 3] + matrix[i + 2][j:j + 3])

        # Update max sum and its position
        if current_sum > max_sum:
            max_sum = current_sum
            max_row, max_col = i, j

# Print the maximum sum
print(f"Sum = {max_sum}")

# Print the 3x3 matrix with maximum sum
for i in range(max_row, max_row + 3):
    print(' '.join(map(str, matrix[i][max_col:max_col + 3])))
