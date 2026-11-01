from functools import cache

with open('2020 input') as file:
    joltages = [int(line.strip()) for line in file]

maxjoltage = max(joltages) + 3
joltages.append(maxjoltage)
joltages.append(0)
joltages.sort()
currjoltage = 0
onejoltdiff = 0
threejoltdiff = 0

for i in joltages:
    if i-currjoltage == 1:
        onejoltdiff += 1
    elif i-currjoltage == 3:
        threejoltdiff += 1

    currjoltage = i

print(f"Part 1: {onejoltdiff * threejoltdiff}")

m1, m2, m3 = joltages[0], joltages[1], joltages[2]

@cache
def rec(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    c = 0
    if num-3 in joltages:
        c += rec(num-3)
    if num-2 in joltages:
        c += rec(num-2)
    if num-1 in joltages:
        c += rec(num-1)

    return c


print(f"Part 2: {rec(max(joltages))}")