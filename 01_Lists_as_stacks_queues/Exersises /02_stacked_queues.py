from collections import deque

numbers = deque()  # Create an empty deque to store the numbers

map_functions = {
    1: lambda x: numbers.append(x[1]),  # x == number_data => [1, 97]
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]  # Get the command and number data

    command = number_data[0]  # Extract the command

    if command in map_functions:
        # If the command is valid and present in the map_functions dictionary, execute the corresponding function
        map_functions[command](number_data)
    else:
        # If the command is not valid, print an error message
        print("Invalid command:", command)

numbers_reversed = reversed(numbers)  # Reverse the deque to print the numbers in reverse order
print(*numbers_reversed, sep=', ')  # Print the reversed numbers separated by commas
