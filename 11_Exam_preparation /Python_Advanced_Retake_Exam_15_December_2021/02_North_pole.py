class SantaWorkshop:
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        self.items = {'D': 0, 'G': 0, 'C': 0}
        self.total_items = sum(row.count('D') + row.count('G') + row.count('C') for row in matrix)
        self.position = [(i, row.index('Y')) for i, row in enumerate(matrix) if 'Y' in row][0]

    def move(self, direction, steps):
        self.matrix[self.position[0]][self.position[1]] = 'x'  # mark the previous position with 'x'

        if direction == 'up':
            self.position = ((self.position[0] - steps) % self.rows, self.position[1])
        elif direction == 'down':
            self.position = ((self.position[0] + steps) % self.rows, self.position[1])
        elif direction == 'left':
            self.position = (self.position[0], (self.position[1] - steps) % self.cols)
        elif direction == 'right':
            self.position = (self.position[0], (self.position[1] + steps) % self.cols)

        # Collect items
        item = self.matrix[self.position[0]][self.position[1]]
        if item in self.items:
            self.items[item] += 1
            self.total_items -= 1

        self.matrix[self.position[0]][self.position[1]] = 'Y'  # mark the current position with 'Y'

        # Check if all items are collected
        if self.total_items == 0:
            print("Merry Christmas!")
            return True
        return False

    def print_state(self):
        print("You've collected:")
        print(f"- {self.items['D']} Christmas decorations")
        print(f"- {self.items['G']} Gifts")
        print(f"- {self.items['C']} Cookies")
        print("Field:")
        for row in self.matrix:
            print(' '.join(row))


# Read size of the workshop
rows, columns = map(int, input().split(', '))

# Initialize workshop
field = []
for _ in range(rows):
    field.append(input().split())
workshop = SantaWorkshop(rows, columns, field)

# Process commands
command = input()
while command != "End":
    direction, steps = command.split('-')
    if workshop.move(direction, int(steps)):
        break
    command = input()

# Print state of the workshop
workshop.print_state()
