from collections import deque   #importing deque so we can work with this function from the library Collections

queue = deque()   #definig the queue variable as a deque

while True:
    name = input()          #asking for the name in the terminal
    if name == "End":       #until the command "End" is given
        print(f"{len(queue)} people remaining.")    #print the leinght of the queue left after End command
        break               #stop the cycle
    elif name == "Paid":    # if "Paid" is given
        while queue:        # enter a cycle
            print(queue.popleft())  #to remove the first item in the queue that means that the last client paid
    else:                   # if the name is not either End or Paid
        queue.append(name)  # append the name to the deque

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
