""""This solution is 80/100 success"""

N = int(input())  # Get the number of queries

stack = []  # Create an empty stack
min_stack = []  # Create an empty stack to track the minimum values
max_stack = []  # Create an empty stack to track the maximum values

for _ in range(N):
    query = input().split()
    operation = query[0]

    if operation == '1':
        number = int(query[1])
        stack.append(number)  # Push the number into the stack

        if not min_stack or number <= min_stack[-1]:
            min_stack.append(number)  # Push the number into the min_stack if it is the new minimum
        if not max_stack or number >= max_stack[-1]:
            max_stack.append(number)  # Push the number into the max_stack if it is the new maximum

    elif operation == '2':
        if stack:
            popped = stack.pop()  # Remove the top number from the stack

            if popped == min_stack[-1]:
                min_stack.pop()  # Remove the top number from the min_stack if it is the minimum
            if popped == max_stack[-1]:
                max_stack.pop()  # Remove the top number from the max_stack if it is the maximum
        else:
            print("Stack is empty")

    elif operation == '3':
        print(max_stack[-1])  # Print the maximum number in the stack

    elif operation == '4':
        print(min_stack[-1])  # Print the minimum number in the stack

stack_formatted = ', '.join(map(str, reversed(stack)))  # Format the stack from top to bottom
print(stack_formatted)  # Print the formatted stack
