clothes = list(map(int, input().split()))  # Get the sequence of integers representing the clothes
rack_capacity = int(input())  # Get the capacity of a rack

rack_count = 1  # Initialize the rack count to 1
current_sum = 0  # Initialize the sum of clothes on the current rack

stack = []  # Create an empty stack to hold the clothes

for cloth in reversed(clothes):  # Iterate through the clothes from the last piece to the first
    if current_sum + cloth <= rack_capacity:  # If adding the cloth does not exceed the rack capacity
        current_sum += cloth  # Add the cloth to the current rack
        stack.append(cloth)  # Push the cloth onto the stack
    else:  # If adding the cloth exceeds the rack capacity
        rack_count += 1  # Increment the rack count
        current_sum = cloth  # Start a new rack with the current cloth
        stack = [cloth]  # Create a new stack with the current cloth

print(rack_count)  # Print the number of racks needed
