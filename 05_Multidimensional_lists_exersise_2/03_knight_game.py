def count_attacks(board, row, col):
    attacks = 0
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < len(board) and 0 <= new_col < len(board) and board[new_row][new_col] == 'K':
            attacks += 1

    return attacks


def remove_knights(board):
    removed = 0

    while True:
        max_attacks = 0
        max_attacks_coords = None

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 'K':
                    attacks = count_attacks(board, row, col)
                    if attacks > max_attacks:
                        max_attacks = attacks
                        max_attacks_coords = (row, col)

        if max_attacks == 0:
            break

        row, col = max_attacks_coords
        board[row][col] = '0'
        removed += 1

    return removed


# Read the size of the board
N = int(input())

# Read the board
board = []
for _ in range(N):
    row = list(input())
    board.append(row)

# Remove knights until no knights that can attack one another with one move are left
removed = remove_knights(board)

# Print the number of knights that need to be removed
print(removed)
