from collections import deque


def process_resources(textiles, medicaments):
    items_created = {"Patch": 0, "Bandage": 0, "MedKit": 0}

    while textiles and medicaments:
        first_textile = textiles.popleft()
        last_medicament = medicaments.pop()

        total = first_textile + last_medicament

        if total in [30, 40, 100]:
            if total == 30:
                item = "Patch"
            elif total == 40:
                item = "Bandage"
            else:
                item = "MedKit"
            items_created[item] += 1
        elif total > 100:
            items_created["MedKit"] += 1
            medicaments[-1] += total - 100
        else:
            medicaments.append(last_medicament + 10)

    return items_created, textiles, medicaments


def print_results(items_created, textiles, medicaments):
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
    elif not textiles:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")

    for item, count in sorted(items_created.items(), key=lambda x: (-x[1], x[0])):
        if count > 0: print(f"{item} - {count}")

    if medicaments: print(f"Medicaments left: {', '.join(map(str, medicaments[::-1]))}")
    if textiles: print(f"Textiles left: {', '.join(map(str, textiles))}")


def main():
    textiles = deque(map(int, input().split()))
    medicaments = list(map(int, input().split()))

    items_created, textiles, medicaments = process_resources(textiles, medicaments)
    print_results(items_created, textiles, medicaments)


if __name__ == "__main__":
    main()
