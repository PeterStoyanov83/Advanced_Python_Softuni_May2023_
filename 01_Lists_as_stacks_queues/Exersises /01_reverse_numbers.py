numbers = input().split()  # Read the string of numbers and split them into a list

stack = []  # Create an empty stack

for number in numbers:
    stack.append(number)  # Push each number onto the stack

reversed_numbers = []
while stack:
    reversed_numbers.append(stack.pop())  # Pop each number from the stack and add it to the reversed numbers list

reversed_string = " ".join(reversed_numbers)  # Join the reversed numbers list into a string with single spaces

print(reversed_string)  # Print the reversed string of numbers
