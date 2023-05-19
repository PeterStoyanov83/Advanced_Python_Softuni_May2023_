# Read the input
n = int(input())
matrix = [list(map(int, input().split(", "))) for _ in range(n)]

# Find the diagonals
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

# Calculate the sums
primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

# Print the results
print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_sum}")
