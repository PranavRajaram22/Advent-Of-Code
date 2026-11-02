from collections import defaultdict, deque
import re
from itertools import product

pattern = re.compile(r'\d+')


memory = defaultdict(int)

with open('2020 input') as file:
    lines = [line.strip() for line in file]

for line in lines:
    if line.startswith('mask'):
        mask = line.split(" ")[2]
        mask = list(mask)
        mask.reverse()
        revmask = deque(mask)
    else:
        line = line.split(" ")
        key = int(re.search(pattern, line[0]).group(0))
        num = int(line[2])
        num = list(bin(num)[2:])

        num.reverse()
        revnum = deque(num)


        while len(revnum) < len(revmask):
            revnum.append('0')

        for i in range(len(revmask)):
            if revmask[i] != 'X':
                revnum[i] = revmask[i]
        revnum.reverse()
        finalnum = ""
        for i in revnum:
            finalnum += i

        num = int(finalnum,2)
        memory[key] = num

print(f"Part 1: {sum(memory.values())}")

memory = defaultdict(int)
for line in lines:
    if line.startswith('mask'):
        mask = line.split(" ")[2]
        mask = list(mask)
        mask.reverse()
        revmask = deque(mask)

    else:
        line = line.split(" ")
        key = int(re.search(pattern, line[0]).group(0))
        num = int(line[2])
        key = list(bin(key)[2:])

        key.reverse()
        revkey = deque(key)

        while len(revkey) < len(revmask):
            revkey.append('0')

        for i in range(len(revmask)):
            if revmask[i] == '1':
                revkey[i] = '1'
            elif revmask[i] == 'X':
                revkey[i] = 'X'

        revkey.reverse()
        key = revkey
        xidx = []
        for i, char in enumerate(key):
            if char == 'X':
                xidx.append(i)

        minput = 0
        maxput = 2**(len(xidx))-1
        combs = []

        for i in range(minput, maxput+1):
            x = deque(str(bin(i)[2:]))
            while len(x) < len(xidx):
                x.appendleft('0')
            combs.append(x)



        for c in combs:
            k = key.copy()
            j = 0
            for i in xidx:
                k[i] = c[j]
                j += 1

            memory[int(str(''.join(k)), 2)] = num


print(f"Part 2: {sum(memory.values())}")




