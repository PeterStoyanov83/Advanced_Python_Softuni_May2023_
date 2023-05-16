from collections import deque

parethesis = deque(input())
open_parethesis = deque()


while parethesis:
    current_parenthesis = parethesis.popleft()
    if current_parenthesis in "([{":
        open_parethesis.append(current_parenthesis)

    elif not open_parethesis:
        print("NO")
        break

    else:
        if f"{open_parethesis.pop() + current_parenthesis}" not in "(){}[]":
            print("NO")
            break
else:
    print("YES")

