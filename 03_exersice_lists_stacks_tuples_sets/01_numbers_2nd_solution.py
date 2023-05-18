first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
# taking the input from the console, splitting it in
# to elements and making a set with these elements FOR BOTH SETS

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    # we will have a list =>  ex... ["Add", "First", 5, 6, 9, 3]

    command = first_command + " " + second_command

    if command == "Add First":
        [first.add(int(element)) for element in data]
        # for element in data:
        #     first.add(int(element))

    elif command == "Add Second":
        [second.add(int(element)) for element in data]
        # for element in data:
        #     second.add(int(element))
    elif command == "Remove First":
        [first.discard(int(element)) for element in data]
        # .discard doesnt raise error if no element in set

    elif command == "Remove Second":
        [second.discard(int(element)) for element in data]

    else:
        print(first.issubset(second) or second.issubset(first))
        # checking if subsets are true or false


print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
