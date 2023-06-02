import random


def make_random_move(stones):
    while True:
        x = random.randint(0, len(stones) - 1)
        y = random.randint(0, len(stones[0]) - 1)
        if stones[x][y] == "":
            return x, y
