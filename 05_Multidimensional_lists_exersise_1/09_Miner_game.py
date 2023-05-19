def is_valid_move(field, row, col):
    return 0 <= row < len(field) and 0 <= col < len(field[0])


def move_miner(field, current_position, direction):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    new_position = (current_position[0] + directions[direction][0],
                    current_position[1] + directions[direction][1])

    return new_position if is_valid_move(field, *new_position) else current_position


# Read the input
field_size = int(input())
commands = input().split()

field = []
miner_position = None
coal_count = 0

for row in range(field_size):
    field.append(input().split())
    if 's' in field[row]:
        miner_position = (row, field[row].index('s'))
    coal_count += field[row].count('c')

# Start the game
for command in commands:
    miner_position = move_miner(field, miner_position, command)
    if field[miner_position[0]][miner_position[1]] == 'c':
        coal_count -= 1
        field[miner_position[0]][miner_position[1]] = '*'
        if coal_count == 0:
            print(f"You collected all coal! {miner_position}")
            break
    elif field[miner_position[0]][miner_position[1]] == 'e':
        print(f"Game over! {miner_position}")
        break
else:
    print(f"{coal_count} pieces of coal left. {miner_position}")
