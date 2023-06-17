from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))
challenges = deque(map(int, input().split()))

while tools and substances and challenges:
    tool = tools[0]
    substance = substances[-1]
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
        tools.popleft()
        substances.pop()
    else:
        tool += 1
        tools.append(tool)
        tools.popleft()
        substance -= 1
        if substance > 0:
            substances[-1] = substance
        else:
            substances.pop()

if len(challenges) == 0:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print("Tools:", ', '.join(map(str, tools)))
if substances:
    print("Substances:", ', '.join(map(str, reversed(substances))))
if challenges:
    print("Challenges:", ', '.join(map(str, challenges)))
