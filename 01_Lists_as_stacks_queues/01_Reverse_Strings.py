text = input()

stack = []
for char in text:
    stack.append(char)

reversed_text = ""
while stack:
    reversed_text += stack.pop()

print(reversed_text)
