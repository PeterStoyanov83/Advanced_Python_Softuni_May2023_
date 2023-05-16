def read_sequence():
    return set(map(int, input().split()))


def process_command(seq1, seq2, command):
    action, _, *nums = command.split()
    nums = set(map(int, nums))

    if action == "Add":
        if command.startswith("Add First"):
            seq1.update(nums)
        elif command.startswith("Add Second"):
            seq2.update(nums)
    elif action == "Remove":
        if command.startswith("Remove First"):
            seq1.difference_update(nums)
        elif command.startswith("Remove Second"):
            seq2.difference_update(nums)
    elif action == "Check":
        print(seq1.issubset(seq2) or seq2.issubset(seq1))


first_sequence = read_sequence()
second_sequence = read_sequence()

n = int(input())
for _ in range(n):
    process_command(first_sequence, second_sequence, input())

print(", ".join(map(str, sorted(first_sequence))))
print(", ".join(map(str, sorted(second_sequence))))
