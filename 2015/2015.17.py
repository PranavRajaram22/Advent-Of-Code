import math
from itertools import combinations

with open('2015 input') as file:
    containers = [int(line.strip()) for line in file]

c = 0
goal = 150
min_num_containers = math.inf
min_containers = []
for i in range(1, len(containers)+1):
    perms = list(combinations(containers, i))
    for k in perms:
        if sum(k) == goal:
            if len(k) < min_num_containers:
                min_num_containers = len(k)
            c += 1


print(f"Part 1: {c}")
t = 0

perms = list(combinations(containers, min_num_containers))
for i in perms:
    if sum(i) == goal:
        t += 1

print(f"Part 2: {t}")