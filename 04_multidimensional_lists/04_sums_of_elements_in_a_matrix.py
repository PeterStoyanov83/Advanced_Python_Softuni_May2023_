rows, columns = map(int, input().split(", "))
matrix = [list(map(int, input().split())) for _ in range(rows)]

column_sums = [sum(row[i] for row in matrix) for i in range(columns)]

for sum_value in column_sums:
    print(sum_value)