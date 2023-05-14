N = int(input())  # Get the number of petrol pumps

petrol_pumps = []  # Create a list to store the petrol pumps

# Read the petrol pump information and add it to the list
for _ in range(N):
    petrol, distance = map(int, input().split())
    petrol_pumps.append((petrol, distance))

start_index = 0  # Start with the first petrol pump

while True:
    current_petrol = 0  # Initialize the current petrol in the tank
    can_complete = True  # Flag to check if the truck can complete the circle

    for i in range(N):
        petrol, distance = petrol_pumps[(start_index + i) % N]
        current_petrol += petrol - distance

        if current_petrol < 0:
            # If the current petrol is negative, the truck cannot reach the next petrol pump
            can_complete = False
            start_index = (start_index + i + 1) % N  # Move to the next petrol pump as the new starting point
            break

    if can_complete:
        # If the truck can complete the circle, the current start_index is the answer
        break

print(start_index)

