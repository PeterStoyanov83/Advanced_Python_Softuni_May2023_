def make_a_move(row, col, field):
    found_hazelnuts = 0

    if not (0 <= row < len(field) and 0 <= col < len(field)):
        return "The squirrel is out of the field."

    if field[row][col] == 't':
        return "Unfortunately, the squirrel stepped on a trap..."

    if field[row][col] == 'h':
        found_hazelnuts += 1

    field[row][col] = '*'
    return found_hazelnuts, field


rows = int(input())
commands = input().split(", ")

field = []
hazelnuts_collected = 0
game_over = False

for _ in range(rows):
    field.append(list(input()))

squirrel_position = []
for row in range(rows):
    for col in range(rows):
        if field[row][col] == 's':
            squirrel_position = [row, col]

field[squirrel_position[0]][squirrel_position[1]] = "*"

for command in commands:
    if command == 'left':
        squirrel_position[1] -= 1
    elif command == 'right':
        squirrel_position[1] += 1
    elif command == 'down':
        squirrel_position[0] += 1
    elif command == 'up':
        squirrel_position[0] -= 1

    result = make_a_move(squirrel_position[0], squirrel_position[1], field)

    if not result:
        game_over = True
        break

    count_hazelnuts, field = result[0], result[1]
    hazelnuts_collected += count_hazelnuts

    if hazelnuts_collected == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not game_over and hazelnuts_collected < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")
