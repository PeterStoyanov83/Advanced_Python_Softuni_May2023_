def find_targets(field):
    targets = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "x":
                targets.append((row, col))
    return targets


def valid_position(field, row, col):
    return 0 <= row < len(field) and 0 <= col < len(field[row])


def move(field, position, direction, steps):
    row, col = position
    if direction == "right":
        col += steps
    elif direction == "left":
        col -= steps
    elif direction == "up":
        row -= steps
    elif direction == "down":
        row += steps

    if valid_position(field, row, col) and field[row][col] == ".":
        position = (row, col)
    return position


def shoot(field, position, direction):
    row, col = position
    if direction == "right":
        for c in range(col + 1, len(field[row])):
            if field[row][c] == "x":
                field[row][c] = "."
                return (row, c)
    elif direction == "left":
        for c in range(col - 1, -1, -1):
            if field[row][c] == "x":
                field[row][c] = "."
                return (row, c)
    elif direction == "up":
        for r in range(row - 1, -1, -1):
            if field[r][col] == "x":
                field[r][col] = "."
                return (r, col)
    elif direction == "down":
        for r in range(row + 1, len(field)):
            if field[r][col] == "x":
                field[r][col] = "."
                return (r, col)
    return None


field = [input().split() for _ in range(5)]
commands_count = int(input())
commands = [input().split() for _ in range(commands_count)]

targets = find_targets(field)
hit_targets = []
row, col = 0, 0  # Set initial position to (0, 0)

for command in commands:
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        row, col = move(field, (row, col), direction, steps)
    elif action == "shoot":
        target = shoot(field, (row, col), direction)
        if target is not None:
            hit_targets.append(target)

if len(hit_targets) == len(targets):
    print(f"Training completed! All {len(targets)} targets hit.")
else:
    print(f"Training not completed! {len(targets) - len(hit_targets)} targets left.")

for target in hit_targets:
    print(f"[{target[0]}, {target[1]}]")
