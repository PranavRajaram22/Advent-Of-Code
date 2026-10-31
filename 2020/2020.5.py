def convert(seat):
    rowinstructions, colinstructions = seat[:-3], seat[-3:]

    rows = list(range(0, 128))
    cols = list(range(0, 9))
    for r in rowinstructions:

        length = len(rows)
        if r == 'F':
            rows = rows[:length//2]
        else:
            rows = rows[length // 2:]


    row = rows[0]

    for c in colinstructions:
        length = len(cols)
        if c == 'L':
            cols = cols[:length//2]
        else:
            cols = cols[length//2:]

    col = cols[0]
    return 8*row + col

with open('2020 input') as file:
    seats = [line.strip() for line in file]

maxid = 0
fullseatids = []
for seat in seats:
    id = convert(seat)
    maxid = max(maxid, id)
    fullseatids.append(id)

print(f'Part 1: {maxid}')

fullseatids.sort()
minid, maxid = min(fullseatids), max(fullseatids)

for id in range(minid, maxid+1):
    if id not in fullseatids:
        print(f"Part 2: {id}")
        break


