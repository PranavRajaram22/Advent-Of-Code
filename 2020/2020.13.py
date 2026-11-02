import math
from copy import deepcopy

with open('2020 input') as file:
    lines = [line.strip() for line in file]

start = int(lines[0])
idsmaster = lines[1].split(",")

ids = deepcopy(idsmaster)

mintimewait = math.inf
mintimeid = 0


for id in ids:
    if id != 'x':
        id = int(id)
        mintime = (start//id + 1)*id

        if mintime-start < mintimewait:
            mintimewait = mintime-start
            mintimeid = id


print(f"Part 1: {mintimewait * mintimeid}")


ids = deepcopy(idsmaster)

offsets = list(range(0, len(ids)))
for i, id in enumerate(ids):
    if id == 'x':
        offsets[i] = -1

a = []
m = ids


while 'x' in m:
    m.remove('x')

m = list(map(int, m))


while -1 in offsets:
    offsets.remove(-1)


for i, mi in enumerate(m):
    a.append(mi-offsets[i])


a[0] = 0
c = []
M = math.prod(m)
for mi in m:
    c.append(M//mi)


def inverse(ci, mi):
    t = 0
    while True:
        x = ci * t
        if x%mi == 1:
            return t

        t += 1



b = []
for i in range(len(c)):
    mi = m[i]
    ci = c[i]

    b.append(inverse(ci, mi))

total = 0

for i in range(len(a)):
    total += (a[i] * b[i] * c[i])

total = total%M

print(f"Part 2: {total}")

