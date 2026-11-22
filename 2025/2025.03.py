from itertools import combinations as comb
with open('2025 input') as file:
    lines = [line.strip() for line in file]

x1 = 0
x2 = 0


def calcmax(num, length):
    maxnum = []

    start = 0
    end = len(num)-length-1
    x = -1

    while len(maxnum) < length:
        if x == -1:
            start = 0
        else:
            start = x + 1
        end += 1
        sub = num[start:end+1]
        x = start + num[start:].index(max(sub))
        maxnum.append(num[x])
    return int(''.join(maxnum))



for line in lines:
    x1 += calcmax(line, 2)
    x2 += calcmax(line, 12)
print(f"Part 1: {x1}")
print(f"Part 2: {x2}")

