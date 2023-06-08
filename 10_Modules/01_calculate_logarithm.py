from math import log

number = int(input())

base = input()

if base == "natural":
    print(f"{log(number):.2f}")

else:
    base = int(input())
    print(f"{log(number,base):.2f}")


