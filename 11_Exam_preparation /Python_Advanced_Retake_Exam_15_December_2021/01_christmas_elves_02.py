"""
1 - reding sequenses
2- while we have elves and materials
    - first elf
    - last material
3 - check if elf is with energy less than 5
    - remove the elf and don't count it as iteration

4 - increment iterations

5 - check if elf is on iteration 3 (creative elf)
    - double material needed
    - double the toys count created

6 - check if elf has energy to create toy
    - update the total amount of material
    - decrease the elf energy
    - give cookie (increase energy + 1)
    - check if iteration is 5
        - no cookies for the elf (decrease elf enegry -1 )
        - current toys count is 0
7 - add toys to total count

8 - append elf in the end of the list

9 - print the output


     """

from collections import deque

elves = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy = 0
total_toys = 0
iterations = 0

while elves and materials:
    elf = elves.popleft()
    material = materials[-1]

    if elf < 5:
        continue
    iterations += 1
    current_toys_count = 0

    if iterations % 3 == 0:
        material *= 2
        

def christmas_elves():
    elf_energies = deque([int(x) for x in input().split(' ')])
    boxes = [int(x) for x in input().split(' ')]

    turns = 0
    toys_made = 0
    total_energy = 0

    while boxes and elf_energies:
        turns += 1

        while elf_energies and elf_energies[0] < 5:
            elf_energies.popleft()

        if not elf_energies:
            break

        box = boxes.pop()
        elf_energy = elf_energies.popleft()

        toys_to_be_created_count = 1
        energy_to_be_spent = box
        energy_increase_factor = 1
        if turns % 3 == 0:
            toys_to_be_created_count = 2
            energy_to_be_spent *= 2
        if turns % 5 == 0:
            toys_to_be_created_count = 0
            energy_increase_factor = 0

        if energy_to_be_spent <= elf_energy:
            toys_made += toys_to_be_created_count
            total_energy += energy_to_be_spent
            elf_energies.append(elf_energy - energy_to_be_spent + energy_increase_factor)
        else:
            boxes.append(box)
            elf_energies.append(elf_energy * 2)

    print(f"Toys: {toys_made}")
    print(f"Energy: {total_energy}")
    if boxes:
        print(f"Boxes left: {', '.join([str(x) for x in boxes])}")
    if elf_energies:
        print(f"Elves left: {', '.join([str(x) for x in elf_energies])}")


christmas_elves()
