import math

from functions_i_use_a_lot import group_by_value
from more_itertools import flatten

with open('2024 input') as file:
    disk = list(map(int, list(file.readline())))


masterexpanse = []


isFile = True
currnum = 0
for num in disk:
    for x in range(num):
        if isFile:
            masterexpanse.append(currnum)
        else:
            masterexpanse.append('.')
    if isFile:
        currnum += 1
    isFile = not isFile

expanse = masterexpanse.copy()
while expanse.count('.') != 0:
    i = expanse.index(".")
    num = expanse.pop(-1)
    if num != '.':
        expanse[i] = num
c = 0


for i in range(len(expanse)):
    c += expanse[i]*i

print(f"Part 1: {c}")

expanse = masterexpanse.copy()
groups = group_by_value(expanse)

try:
    maxnum = int(groups[-1][0])
except ValueError:
    maxnum = int(groups[-2][0])

for num in range(maxnum, -1, -1):

    for i in range(len(groups)-1, -1, -1):
        group = groups[i]
        if group[0] == num:
            currgroup = group
            curridx = i
            break
    for j, group in enumerate(groups):
        if group[0] == '.' and len(group) >= len(currgroup) and curridx > j:
            for x in range(len(currgroup)-1, -1, -1):
                group[group.index(".")], currgroup[x] = currgroup[x], group[group.index(".")]
            break
    groups = group_by_value(list(flatten(groups)))

expanse = list(flatten(groups))

c = 0

for i in range(len(expanse)):
    if expanse[i] != '.':
        c += expanse[i]*i

print(f"Part 2: {c}")
