rows, columns = map(int, input().split(", "))
matrix = []
max_sum = float("-inf")
max_submatrix = []

# Read the matrix
for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

# Find the submatrix with the maximum sum
for row in range(rows - 1):
    for col in range(columns - 1):
        submatrix = [
            [matrix[row][col], matrix[row][col + 1]],
            [matrix[row + 1][col], matrix[row + 1][col + 1]],
        ]
        submatrix_sum = sum(sum(submatrix, []))
        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            max_submatrix = submatrix

# Print the result
for row in max_submatrix:
    print(" ".join(str(num) for num in row))
print(max_sum)
