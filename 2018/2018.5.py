import math
from copy import copy

with open('2018 input') as file:
    polymer = file.readline()

i = 0

def func(polymer):
    newpolymer = ""
    destroyed = False
    while not destroyed:
        i = 0
        while i < len(polymer):
            if len(polymer[i:i+2]) == 2 and abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
                i += 2
                destroyed = True

            else:
                newpolymer += polymer[i]
                i += 1

        polymer = newpolymer
        newpolymer = ""
        if not destroyed:
            break
        destroyed = False
    return len(polymer)

print(f"Part 1: {func(polymer)}")


with open('2018 input') as file:
    masterpolymer = file.readline()


minlen = math.inf
for char in range(ord('a'), ord('z')+1):
    polymer = copy(masterpolymer)
    lower = str(chr(char))
    upper = str(lower.upper())
    polymer = polymer.replace(lower, "")
    polymer = polymer.replace(upper, "")
    length = func(polymer)
    minlen = min(minlen, length)

print(f"Part 2: {minlen}")