n, m = [int(num) for num in input().split()]

first_set = {int(input()) for _ in range(n)}
second_set = {int(input()) for _ in range(m)}

print(*first_set.intersection(second_set), sep="\n")


"""Ths syntax is only for sets. not comparing sets with something else!!!"""

print(first_set & second_set)   #"the items present in both sets"
print(first_set | second_set)   #"nioning them together"
print(first_set - second_set)   #"the difference between the two sets"
print(first_set ^ second_set)   #"symetric difference between the two sets"
