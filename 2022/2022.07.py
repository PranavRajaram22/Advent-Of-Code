from collections import defaultdict
from functools import cache

with open('2022 input') as file:
    lines = [line.strip() for line in file]


graph = defaultdict(list)

currpath = []
sizes = dict()
dirs = set('/')

i = 0
while i < len(lines):
    line = lines[i].split(' ')
    i += 1

    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                currpath.pop(-1)
            elif line[2] == '/':
                currpath = ['/']
            else:
                currpath.append(line[2])

        elif line[1] == 'ls':
            while i < len(lines) and lines[i].split(" ")[0] != '$':
                graph[tuple(currpath)].append(lines[i].split(' ')[1])
                if lines[i].split(" ")[0] == 'dir':
                    dirs.add(lines[i].split(" ")[1])
                else:
                    sizes[tuple(currpath) + (lines[i].split(" ")[1], )] = int(lines[i].split(' ')[0])
                i += 1

@cache
def rec(currpath):
    if currpath in sizes.keys():
        return sizes[currpath]
    else:
        c = 0
        for i in graph[currpath]:
            c += rec(tuple([*currpath + (i,)]))
        return c


c = 0

dirsizes = dict()
for path in graph:
    r = rec(path)
    dirsizes[path] = r
    if r < 100000:
        c += r


print(f'Part 1: {c}')
filesize = dirsizes[('/',)]
dirsizes = list(dirsizes.values())
dirsizes.sort()

currentfreedspace = 70000000-filesize

for s in dirsizes:
    if currentfreedspace + s >= 30000000:
        print(f"Part 2: {s}")
        break