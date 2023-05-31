import os

while True:
    command = input()

    if command == "End":
        break

    command_parts = command.split("-")
    action = command_parts[0]
    file_name = command_parts[1]

    if action == "Create":
        with open(file_name, 'w') as file:
            pass
    elif action == "Add":
        content = command_parts[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif action == "Replace":
        old_string = command_parts[2]
        new_string = command_parts[3]

        try:
            with open(file_name, 'r') as file:
                file_content = file.read()

            file_content = file_content.replace(old_string, new_string)

            with open(file_name, 'w') as file:
                file.write(file_content)
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
