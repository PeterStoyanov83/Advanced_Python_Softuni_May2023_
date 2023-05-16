""" solution optimised with functions """

from collections import deque
from datetime import datetime, timedelta


def get_next_time(current_time):
    return current_time + timedelta(seconds=1)


def get_robot_data(robots_data):
    robot_info = {}
    for robot in robots_data:
        robot_name, process_time = robot.split("-")
        robot_info[robot_name] = [int(process_time), None]
    return robot_info


def process_products(robot_info, start_time, products):
    current_time = start_time
    while products:
        current_time = get_next_time(current_time)
        for robot in robot_info:
            if robot_info[robot][1] == current_time:
                robot_info[robot][1] = None

        product = products.popleft()
        for robot in robot_info:
            if robot_info[robot][1] is None:
                robot_info[robot][1] = current_time + timedelta(seconds=robot_info[robot][0])
                print(f"{robot} - {product} [{current_time.strftime('%H:%M:%S')}]")
                break
        else:
            products.append(product)


robots_data = input().split(";")
start_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

robot_info = get_robot_data(robots_data)
process_products(robot_info, start_time, products)
