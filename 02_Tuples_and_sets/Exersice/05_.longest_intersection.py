n = int(input())

intersections = []

for _ in range(n):
    data = input().split("-")
    first_sequence = [int(el) for el in data[0].split(",")]
    second_sequence = [int(el) for el in data[1].split(",")]
    intersection = set(range(first_sequence[0], first_sequence[1] + 1)).intersection(
        set(range(second_sequence[0], second_sequence[1] + 1)))
    intersections.append(intersection)

longest_intersection = sorted(intersections, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
