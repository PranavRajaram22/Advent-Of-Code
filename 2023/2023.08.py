import time
from math import lcm

from functions_i_use_a_lot import group_list_by_empty_line


with open('2023 input') as file:
    lines = [line.strip() for line in file]

directions, n = group_list_by_empty_line(lines)
directions = directions[0]
nodes = dict()

for i in n:
    i = i.split(" ")
    i[2] = i[2][1:-1]
    i[3] = i[3][:-1]
    nodes[i[0]] = (i[2], i[3])

curr = 'AAA'

steps = 0
idx = 0
while curr != 'ZZZ':
    if directions[idx] == 'R':
        curr = nodes[curr][1]
    else:
        curr = nodes[curr][0]

    steps += 1
    idx = (idx+1)%len(directions)

print(f"Part 1: {steps}")
curr = []
for node in nodes.keys():
    if node[-1] == 'A':
        curr.append(node)

allsteps = []
for node in curr:
    steps = 0
    idx = 0

    while not (node[-1] == 'Z'):
        if directions[idx] == 'R':
            node = nodes[node][1]
        else:
            node = nodes[node][0]

        steps += 1
        idx = (idx+1)%len(directions)

    allsteps.append(steps)

print(f"Part 2: {lcm(*allsteps)}")
