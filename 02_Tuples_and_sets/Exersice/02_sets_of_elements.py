n, m = map(int, input().split())

set_n = set()
set_m = set()

for _ in range(n):
    number = int(input())
    set_n.add(number)

for _ in range(m):
    number = int(input())
    set_m.add(number)

common_elements = set_n & set_m

for element in common_elements:
    print(element)
