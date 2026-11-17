import math
from zipimport import cp437_table

with open('2021 input') as file:
    crabs = list(map(int, file.readline().strip().split(",")))



def fuelsum(crabs, pos):
    total = 0
    for crab in crabs:
        total += abs(crab-pos)

    return total


small, big = min(crabs), max(crabs)

mintotal = math.inf
mipos = None

for pos in range(small, big+1):
    f = fuelsum(crabs, pos)
    if f < mintotal:
        mintotal = f
        minpos = pos


print(f"Part 1: {mintotal}")

def fuelsumpart2(crabs, pos:int):
    total = 0

    for crab in crabs:
        n = abs(pos-crab)
        total += int(n*(n+1)/2)

    return total


mintotal = math.inf
mipos = None

for pos in range(small, big+1):
    f = fuelsumpart2(crabs, pos)
    if f < mintotal:
        mintotal = f
        minpos = pos

print(f"Part 2: {mintotal}")