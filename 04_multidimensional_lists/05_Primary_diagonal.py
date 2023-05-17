N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

diagonal_sum = sum(matrix[i][i] for i in range(N))

print(diagonal_sum)
