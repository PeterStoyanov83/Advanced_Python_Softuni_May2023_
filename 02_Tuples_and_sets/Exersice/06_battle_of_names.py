n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // row
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set == sum_even_set:
    union_values = odd_set.union(even_set)
    print(", ".join([str(el) for el in union_values]))
elif sum_odd_set > sum_even_set:
    different_values = odd_set.difference(even_set)
    print(", ".join([str(el) for el in different_values]))
else:
    symmetric_different_values = odd_set.symmetric_difference(even_set)
    print(", ".join([str(el) for el in symmetric_different_values]))
