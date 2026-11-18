from collections import defaultdict


with open('2022 input') as file:
    lines = [line.strip() for line in file]

tailvisited = []
def updateTail(visited, hx, hy, tx, ty):
    for hyi in range(hy-1, hy+2):
        for hxi in range(hx-1, hx+2):
            if tx == hxi and ty == hyi:
                visited.append((tx, ty))
                return (visited, hx, hy, tx, ty)

    #not nearby: need to update tail pos

    #is aligned
    if (hy-2 == ty and hx == tx): #aligned in x, while ty < hy
        ty += 1
    elif (hy+2 == ty and hx == tx): #aligned in x, while ty > hy
        ty -= 1
    elif (hy == ty and hx-2 == tx): #aligned in y, while tx < hx
        tx += 1
    elif (hy == ty and hx+2 == tx): #aligned in y, while tx > hx:
        tx -= 1

    #not aligned. need to move diagonally.

    elif hx >= tx and hy >= ty: #head is upright. move tail upright
        tx += 1
        ty += 1

    elif hx >= tx and hy <= ty: #head is downright. move tail downright
        tx += 1
        ty -= 1

    elif hx <= tx and hy >= ty: #head is upleft. move tail upleft
        tx -= 1
        ty += 1

    elif hx <= tx and hy <= ty: #head is downleft. move tail downleft
        tx -= 1
        ty -= 1

    visited.append((tx, ty))
    return (visited, hx, hy, tx, ty)

hx, hy, tx, ty = 0, 0, 0, 0
for line in lines:
    dir, mag = line.split(" ")
    mag = int(mag)
    if dir == 'R':
        for _ in range(mag):
            hx += 1
            tailvisited, hx, hy, tx, ty = updateTail(tailvisited, hx, hy, tx, ty)
    elif dir == 'L':
        for _ in range(mag):
            hx -= 1
            tailvisited, hx, hy, tx, ty = updateTail(tailvisited, hx, hy, tx, ty)
    elif dir == 'U':
        for _ in range(mag):
            hy += 1
            tailvisited, hx, hy, tx, ty = updateTail(tailvisited, hx, hy, tx, ty)

    elif dir == 'D':
        for _ in range(mag):
            hy -= 1
            tailvisited, hx, hy, tx, ty = updateTail(tailvisited, hx, hy, tx, ty)

print(f'Part 1: {len(set(tailvisited))}')

coords = dict()

for headnum in range(0, 10):
    coords[headnum] = [0, 0, []]

hx, hy = 0, 0
coords[0] = [hx, hy , []]

def updateTails():
    for headnum in range(9):
        tailnum = headnum+1
        hx, hy, tx, ty, visited = *coords[headnum][:2], *coords[tailnum]
        visited, hx, hy, tx, ty = updateTail(visited, hx, hy, tx, ty)
        coords[headnum][:2] = [hx, hy]
        coords[tailnum] = [tx, ty, visited]
    return coords

for line in lines:
    dir, mag = line.split(" ")
    mag = int(mag)
    if dir == 'R':
        for _ in range(mag):
            hx += 1
            coords[0][0] = hx
            coords[0][2].append((hx, hy))
            coords = updateTails()
    elif dir == 'L':
        for _ in range(mag):
            hx -= 1
            coords[0][0] = hx

            coords = updateTails()
    elif dir == 'U':
        for _ in range(mag):
            hy += 1
            coords[0][1] = hy

            coords = updateTails()

    elif dir == 'D':
        for _ in range(mag):
            hy -= 1
            coords[0][1] = hy

            coords = updateTails()



allvisited = []
print(f'Part 2: {len(set(coords[9][2]))}')
