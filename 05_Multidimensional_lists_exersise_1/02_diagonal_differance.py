# Read the input
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Find the diagonals
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

# Calculate the sums
primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

# Calculate and print the absolute difference
difference = abs(primary_sum - secondary_sum)
print(difference)