import math
from copy import copy
from itertools import batched

from more_itertools import flatten

from functions_i_use_a_lot import group_list_by_empty_line

with open('2023 input') as file:
    lines = [line.strip() for line in file]

seeds = lines.pop(0)
lines.pop(0)

lines = group_list_by_empty_line(lines)


seeds = seeds.split(" ")[1:]
seeds = list(map(int, seeds))
for i, line in enumerate(lines):
    line.pop(0)
    for j, m in enumerate(line):
        line[j] = list(map(int, m.split(" ")))
    lines[i] = line

def transfer(seed, lines):
    for line in lines:
        dest_start, source_start, length = line
        if source_start <= seed < source_start + length:
            return seed-source_start + dest_start

    return seed


locations = []
for seed in seeds:
    for map in lines:
        seed = transfer(seed, map)
    locations.append(seed)

print(f'Part 1: {min(locations)}')
seeds = list(batched(seeds, 2))


def transfer2(seed_start, seed_length, map, i):
    try:
        line = map[i]
        dest_start, source_start, length = line
        source_end = source_start + length - 1 #if seed == source end, that counts as inside the set
        seed_end = seed_start + seed_length - 1
    except IndexError:
        #case 0: i is not in range of the map. this becomes the base case. every other case eventualy hits this case.
        return [(seed_start, seed_length)]

    #case 1: ranges do not overlap at all

    #case 1.1 seed range is entirely below the source range

    if seed_end < source_start:
        return transfer2(seed_start, seed_length, map, i+1)
    #case 1.2 seed range is entirely above the source range

    elif seed_start > source_end:
        return transfer2(seed_start, seed_length, map, i+1)

    #case 2: seed range is entirely inside of the source range (this includes if the two ranges are equal)

    elif seed_start >= source_start and seed_end <= source_end:
        seed_start = seed_start - source_start + dest_start
        return [(seed_start, seed_length)]

    #case 3: seed range entirely contains the source_range (this does not include if the two ranges are equal)

    elif seed_start < source_start and source_end < seed_end:

        newseeds = []

        #need to add 3 ranges to this seed, and all can use recursion

        #first range to consider is the part of the seed range that equals the source range.
        #use recursion to make this part of the range hit case 2 and add the new part of this range
        #to newseeds

        #we can just call the transfer on the same map line and then add its range to newseeds
        x = transfer2(source_start, length, map, i)
        for l in x:
            newseeds.append(l)

        #second range to consider is the aprt of the seed range that is entirely below the source range.
        #use recursion, but increase the line to now apply that seed range to the next line

        x = transfer2(seed_start, source_start-seed_start, map, i+1)
        for l in x:
            newseeds.append(l)

        #final range to consider is the part of the seed_range that is entirely above the source range
        #again use recusion, and increase the line to now apply that seed range to the next line

        x = transfer2(source_end+1, seed_end-source_end, map, i+1)
        for l in x:
            newseeds.append(l)

        return newseeds

    #case 4: seed range is partially inside of the source range and partially below the source range

    #split the seed range into 2 parts; one thats entirely inside of the soure range and then will get hit by case 2, and the other part that will get hit by case 1.1

    elif seed_start < source_start and source_end >= seed_end >= source_start:
        newseeds = []

        #first range: one thats entirely inside of the source range. this range can be called recursively on the next line and will immediately get hit by case 2

        x = transfer2(source_start, seed_end-source_start+1, map, i)
        for l in x:
            newseeds.append(l)

        #second range: one thats entirey below the source range. this range can also be called recursively, and may or may not be actually transfered.

        x = transfer2(seed_start, source_start-seed_start, map, i+1)
        for l in x:
            newseeds.append(l)

        return newseeds

    #case 5: seed range is partially inside of the source range and partially above the source range

    elif source_end >= seed_start >= source_start and seed_end > source_end:

        newseeds = []
        #similar to case 4.

        #first range: the one tahts entirely inside of the soruce range.
        x = transfer2(seed_start, source_end-seed_start + 1, map, i)
        for l in x:
            newseeds.append(l)

        #second range: the one thats entirely above the source range
        x = transfer2(source_end+1, seed_end-source_end, map, i+1)
        for l in x:
            newseeds.append(l)


        return newseeds



locs = []
for map in lines:
    newseeds = []
    for seed in seeds:
        x = transfer2(*seed, map, 0)
        for i in x:
            newseeds.append(i)

    seeds = newseeds.copy()

for x in seeds:
    locs.append(x[0])


print(f'Part 2: {min(locs)}')

