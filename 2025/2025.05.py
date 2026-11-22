from itertools import batched

from more_itertools import flatten

from functions_i_use_a_lot import group_list_by_empty_line

with open('2025 input') as file:
    lines = [line.strip() for line in file]

ranges, ids = group_list_by_empty_line(lines)
ids = list(map(int, ids))
for i, rang in enumerate(ranges):
    ranges[i] = list(map(int, rang.split('-')))



c = 0

for id in ids:
    for r in ranges:
        if r[0] <= id and id <= r[1]:
            c += 1
            break

print(f"Part 1: {c}")



ranges = sorted(ranges, key=lambda x: x[1])
i = 0
while i < len(ranges)-1:
    x, y = ranges[i], ranges[i+1]
    if x[1] >= y[0]:
        ranges[i] = [min(x[0], y[0]), max(x[1], y[1])]
        ranges.pop(i+1)
        i = 0
    else:
        i += 1


c = 0
for r in ranges:
    c += r[1] - r[0] + 1

print(f"Part 1: {c}")
'''
wrong answers:
7417861346623 --> too low
18610907783093 --> too low
347349501282222 --> too low
359913027576322

'''