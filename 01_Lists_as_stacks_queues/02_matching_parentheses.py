stack_parent = []

text = input()

for index in range(len(text)):
    if text[index] == '(':
        stack_parent.append(index)
        "filinng up the stack until the next parenteses"
    elif text[index] == ')':
        start_position = stack_parent.pop()
        end_position = index + 1
    print(text[start_position:end_position])
