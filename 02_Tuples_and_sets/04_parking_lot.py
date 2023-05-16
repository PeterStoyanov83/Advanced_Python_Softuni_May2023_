# Read the number of commands from the input
n = int(input())

# Create an empty set to store the car numbers
parking_lot = set()

# Go through each command
for _ in range(n):
    # Read the command from the input
    direction, car_number = input().split(", ")

    # If the direction is "IN", add the car number to the set
    if direction == "IN":
        parking_lot.add(car_number)
    # If the direction is "OUT", remove the car number from the set
    elif direction == "OUT":
        parking_lot.discard(car_number)

# If the parking lot is empty, print a special message
if not parking_lot:
    print("Parking Lot is Empty")
# Otherwise, print each car number that is still in the parking lot
else:
    for car_number in parking_lot:
        print(car_number)
