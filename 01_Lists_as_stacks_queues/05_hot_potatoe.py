from collections import deque

kids = input().split()  # Get the names of the kids and split them into a list
toss_count = int(input())  # Get the value of n for the nth toss

circle = deque(kids)  # Create a deque using the list of kids

while len(circle) > 1:
    for _ in range(toss_count - 1):  # Perform n - 1 tosses
        circle.append(circle.popleft())  # Rotate the circle by moving the first kid to the end

    removed_kid = circle.popleft()  # Remove the nth kid from the circle
    print(f"Removed {removed_kid}")  # Print the removed kid's name

last_kid = circle[0]  # The last remaining kid in the circle
print(f"Last is {last_kid}")  # Print the last kid's name

"""Solution with rotate method"""
# from collections import deque
#
# kids = input().split()  # Get the names of the kids and split them into a list
# toss_count = int(input())  # Get the value of n for the nth toss
#
# circle = deque(kids)  # Create a deque using the list of kids
#
# while len(circle) > 1:
#     circle.rotate(-toss_count + 1)  # Rotate the circle by moving the first kid to the end
#
#     removed_kid = circle.popleft()  # Remove the nth kid from the circle
#     print(f"Removed {removed_kid}")  # Print the removed kid's name
#
# last_kid = circle[0]  # The last remaining kid in the circle
# print(f"Last is {last_kid}")  # Print the last kid's name
