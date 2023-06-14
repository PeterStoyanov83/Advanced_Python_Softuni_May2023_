from collections import deque

starting_quantity = int(input())

queue = deque()

while True:
    command = input()
    if command == "Start":
        break

    if command.startswith("refill"):
        refill_liters = int(command.split()[1])
        starting_quantity += refill_liters

    else:
        liters_needed = int(command)
        person = queue.popleft()
        if liters_needed <= starting_quantity:
            starting_quantity -= liters_needed
            print(f"{person} got water")

        else:
            print(f"{person} must wait")

print(f"{starting_quantity} liters left")
