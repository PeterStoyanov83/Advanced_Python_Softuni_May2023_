# Read matrix dimensions
rows = int(input())

# Read the matrix elements
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Process commands
while True:
    command = input()
    if command == "END":
        break

    # Parse the command
    command_parts = command.split()
    action = command_parts[0]
    row = int(command_parts[1])
    col = int(command_parts[2])
    value = int(command_parts[3])

    # Check if the coordinates are valid
    if not (0 <= row < rows and 0 <= col < len(matrix[row])):
        print("Invalid coordinates")
        continue

    # Perform the action based on the command
    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

# Print the updated matrix
for row in matrix:
    print(*row)
