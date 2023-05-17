N = int(input())
matrix = [list(input()) for _ in range(N)]
symbol = input()

found = False

for row in range(N):
    for col in range(N):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
