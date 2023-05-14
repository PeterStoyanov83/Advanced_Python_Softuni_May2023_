from collections import deque

food_quantity = int(input())  # Get the quantity of food for the day
orders = deque(map(int, input().split()))  # Get the sequence of orders and create a queue

biggest_order = max(orders)  # Find the biggest order

while orders:
    current_order = orders.popleft()  # Get the first order from the queue

    if current_order <= food_quantity:
        food_quantity -= current_order  # Reduce the food quantity
    else:
        orders.appendleft(current_order)  # Put the order back in the queue
        break

if not orders:
    print(biggest_order)
    print("Orders complete")
else:
    orders_left = ' '.join(map(str, orders))
    print(biggest_order)
    print(f"Orders left: {orders_left}")
