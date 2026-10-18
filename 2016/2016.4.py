from collections import Counter, defaultdict

c = 0

with open('2016 input') as file:
    rooms = [line.strip() for line in file]

realrooms = [("qzmtzixmtkozyivhz",343)]

for room in rooms:
    room = room.split("[")
    room[-1] = room[-1][:-1]
    checksum = room.pop(-1)

    room = room[0].split("-")
    id = int(room.pop(-1))
    name = ""
    for i in room:
        name += i

    count = Counter(name)
    d = defaultdict(list)
    for key in count.keys():
        d[count[key]].append(key)
        d[count[key]].sort()
    m = max(d.keys())
    realchecksum = ""
    for x in range(m, -1, -1):
        for char in d[x]:
            realchecksum += char

    realchecksum = realchecksum[:5]
    if realchecksum == checksum:
        c += id
        realrooms.append((name, id))

print(f"Part 1: {c}")


def rotate(name, id):
    name = list(map(ord, list(name)))
    for i, x in enumerate(name):
        name[i] = chr((x-96 + id)%26 + 96)

    l = ""
    for i in name:
        l += i
    return l


for room in realrooms:
    name, id = room
    name = rotate(name, id)
    print(name, id)

