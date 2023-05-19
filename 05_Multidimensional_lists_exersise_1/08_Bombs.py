def is_valid_position(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


# Read the input
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bombs = [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in input().split()]

# Define the directions in which a bomb can explode
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1, 0), (1, 1)
]

# Explode the bombs
for bomb in bombs:
    bomb_row, bomb_col = bomb
    bomb_value = matrix[bomb_row][bomb_col]
    if bomb_value > 0:
        for direction in directions:
            new_row, new_col = bomb_row + direction[0], bomb_col + direction[1]
            if is_valid_position(matrix, new_row, new_col) and matrix[new_row][new_col] > 0:
                matrix[new_row][new_col] -= bomb_value
        matrix[bomb_row][bomb_col] = 0

# Count the alive cells and their sum
alive_cells = [cell for row in matrix for cell in row if cell > 0]
count_alive_cells = len(alive_cells)
sum_of_cells = sum(alive_cells)

# Print the results
print(f"Alive cells: {count_alive_cells}")
print(f"Sum: {sum_of_cells}")
for row in matrix:
    print(' '.join(map(str, row)))
