from collections import deque
from itertools import islice

with open('2021 input') as file:
    depths = list(map(int, [line.strip() for line in file]))

c = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        c += 1


print(f"Part 1: {c}")

sums = []

def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 3) → ABC BCD CDE DEF EFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)

for i in sliding_window(depths, 3):
    sums.append(sum((i)))

c = 0

for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        c += 1

print(f"Part 2: {c}")