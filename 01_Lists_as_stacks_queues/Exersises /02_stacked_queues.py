from collections import deque

numbers = deque()  # Create an empty deque to store the numbers

# Process the input commands
for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]  # Get the command and number data
    command = number_data[0]  # Extract the command

    # Process different commands
    if command == 1:
        numbers.append(number_data[1])  # Command 1: Add the number to the deque
    elif command == 2:
        if numbers:
            numbers.pop()  # Command 2: Remove the last number from the deque if it's not empty
    elif command == 3:
        if numbers:
            print(max(numbers))  # Command 3: Print the maximum number in the deque if it's not empty
    elif command == 4:
        if numbers:
            print(min(numbers))  # Command 4: Print the minimum number in the deque if it's not empty

numbers_reversed = reversed(numbers)  # Reverse the deque to print the numbers in reverse order
print(*numbers_reversed, sep=', ')  # Print the reversed numbers separated by commas
