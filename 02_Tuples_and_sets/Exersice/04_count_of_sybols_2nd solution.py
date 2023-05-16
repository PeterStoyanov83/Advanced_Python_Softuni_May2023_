

char_counts = {}

for char in input():
    char_counts[char] = char_counts.get(char, 0) + 1
    if char not in char_counts:
        char_counts[char] = 0

    char_counts[char] += 1

for char, count in sorted(char_counts.items()):
    print(f"{char}: {count} time/s")
