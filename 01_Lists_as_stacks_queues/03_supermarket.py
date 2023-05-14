from collections import deque

queue = deque()

while True:
    name = input()
    if name == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif name == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)

# name = input()
# customers = deque
#
# while name != "Paid":
#     customers.append(name)
#     name = input()
#
# while customers:
#     print(customers.popleft())
#
# name = input()
#
# while name != "End":
#     customers.append(name)
#     name = input()
#
# print(len(customers))
