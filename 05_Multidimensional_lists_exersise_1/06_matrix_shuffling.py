# Read the input
rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

# Read commands
while True:
    command = input().split()

    # If the command is "END", stop the program
    if command[0] == "END":
        break

    # If the command is not valid, print "Invalid input!"
    elif (command[0] != "swap" or len(command) != 5 or
          not command[1].isdigit() or not command[2].isdigit() or
          not command[3].isdigit() or not command[4].isdigit() or
          int(command[1]) < 0 or int(command[2]) < 0 or
          int(command[3]) < 0 or int(command[4]) < 0 or
          int(command[1]) >= rows or int(command[3]) >= rows or
          int(command[2]) >= cols or int(command[4]) >= cols):
        print("Invalid input!")
    else:
        # If the command is valid, swap the values and print the matrix
        row1, col1, row2, col2 = map(int, command[1:])
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(' '.join(row))
