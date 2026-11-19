from collections import deque
from itertools import islice, zip_longest

with open('2024 input') as file:
    lines = [list(line.strip()) for line in file]




def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 3) → ABC BCD CDE DEF EFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)

#check across
across = 0
for row in lines:
    pos = list(sliding_window(row, 4))
    across += pos.count(tuple('XMAS')) + pos.count(tuple("SAMX"))
#check columns
down = 0
transpose = list(zip_longest(*lines))
for row in transpose:
    pos = list(sliding_window(row, 4))
    down += pos.count(tuple('XMAS')) + pos.count(tuple("SAMX"))

right = 0
left = 0
for y in range(len(lines)-3):
    for x in range(len(lines[0])-3):
        char = lines[y][x]
        diagonal = ''
        for i in range(4):
            diagonal += lines[y+i][x+i]

        if diagonal == 'XMAS' or diagonal == 'SAMX':
            right += 1


    for x in range(3, len(lines[0])):
        char = lines[y][x]

        diagonal = ''
        for i in range(4):
            diagonal += lines[y+i][x-i]


        if diagonal == 'XMAS' or diagonal == 'SAMX':
            left += 1


print(f'Part 1: {across+down+left+right}')
c = 0
for y in range(1, len(lines)-1):
    for x in range(1, len(lines[0])-1):
        if lines[y][x] == 'A':
            tr, br, tl, bl = lines[y-1][x+1], lines[y+1][x+1], lines[y-1][x-1], lines[y+1][x-1]
            if all(i in ['M', 'S'] for i in [tl, br, tr, bl]) and tl != br and tr != bl:
                c += 1

print(f"Part 2: {c}")

