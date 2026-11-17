from collections import Counter, defaultdict

with open('2021 input') as file:
    fish = list(map(int, file.readline().split(",")))

c = Counter(fish)
fishes = dict()
for k, v in c.items():
    fishes[k] = v



for _ in range(80):
    newfishes = dict()
    try:
        num0 = fishes[0]
    except KeyError:
        num0 = 0

    for day in range(1, 9):
        try:
            newfishes[day-1] = fishes[day]
        except KeyError:
            pass

    try:
        newfishes[6] += num0
    except KeyError:
        newfishes[6] = num0

    try:
        newfishes[8] += num0
    except KeyError:
        newfishes[8] = num0

    fishes = newfishes

print(f'Part 1: {sum(newfishes.values())}')

for _ in range(256-80):
    newfishes = dict()
    try:
        num0 = fishes[0]
    except KeyError:
        num0 = 0

    for day in range(1, 9):
        try:
            newfishes[day-1] = fishes[day]
        except KeyError:
            pass

    try:
        newfishes[6] += num0
    except KeyError:
        newfishes[6] = num0

    try:
        newfishes[8] += num0
    except KeyError:
        newfishes[8] = num0

    fishes = newfishes

print(f'Part 2: {sum(newfishes.values())}')