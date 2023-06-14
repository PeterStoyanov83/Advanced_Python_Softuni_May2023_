def play_blind_mans_buff(playground):
    n, m = len(playground), len(playground[0])
    position = find_initial_position(playground)
    touched_opponents = 0
    moves_made = 0

    while True:
        direction = input()
        if direction == "Finish":
            break

        new_position = get_new_position(position, direction)

        if is_within_playground(new_position, n, m):
            cell_content = get_cell_content(playground, new_position)

            if cell_content == '-':
                moves_made += 1
                position = new_position
            elif cell_content == 'P':
                touched_opponents += 1
                moves_made += 1
                position = new_position

    print("Game over!")
    print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


def find_initial_position(playground):
    for i in range(len(playground)):
        for j in range(len(playground[i])):
            if playground[i][j] == 'B':
                return (i, j)


def get_new_position(position, direction):
    i, j = position
    if direction == 'up':
        return (i - 1, j)
    elif direction == 'down':
        return (i + 1, j)
    elif direction == 'left':
        return (i, j - 1)
    elif direction == 'right':
        return (i, j + 1)
    else:
        return position


def is_within_playground(position, n, m):
    i, j = position
    return 0 <= i < n and 0 <= j < m


def get_cell_content(playground, position):
    i, j = position
    return playground[i][j]


# Read input
n, m = map(int, input().split())
playground = []
for _ in range(n):
    row = input().split()
    playground.append(row)

# Play the game
play_blind_mans_buff(playground)