n = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(n):
    reservation_number = input()
    if reservation_number[0].isdigit():
        vip_guests.add(reservation_number)
    else:
        regular_guests.add(reservation_number)

guest_arrival = input()
while guest_arrival != "END":
    if guest_arrival in vip_guests:
        vip_guests.remove(guest_arrival)
    elif guest_arrival in regular_guests:
        regular_guests.remove(guest_arrival)
    guest_arrival = input()

all_guests = sorted(vip_guests) + sorted(regular_guests)
print(len(all_guests))
[print(guest) for guest in all_guests]
