from collections import deque

clothes = deque([int(x) for x in input().split()])  # Get the sequence of integers representing the clothes

rack_capacity = int(input())  # Get the capacity of a rack

racks_count = 1  # Initialize the rack count to 1
current_rack_space = rack_capacity  # Initialize the sum of clothes on the current rack

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth

    else:
        racks_count += 1
        current_rack_space = rack_capacity - cloth

print(racks_count)
