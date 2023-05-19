# reading the matrix
rows, cols = map(int, input().split())
matrix = [list(input().split()) for _ in range(rows)]

# initialising counter
count = 0

for i in range(rows - 1):  
    for j in range(cols - 1):  
        # Check if all elements in the 2x2 square are the same
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            count += 1


print(count)
