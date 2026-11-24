from copy import copy
from itertools import batched

with open('2017 input.txt') as file:
    lengths = list(map(int, file.readline().strip().split(",")))



nums = list(range(256)) #change to 256

skipsize = 0
currpos = 0

for length in lengths:
    sublist_to_reverse = []
    for i in range(currpos, currpos+length):
        sublist_to_reverse.append(nums[i%len(nums)])
    sublist_to_reverse.reverse()
    for i in range(currpos, currpos+length):
        nums[i%len(nums)] = sublist_to_reverse[i-currpos]

    currpos += length + skipsize
    skipsize += 1


print(f"Part 1: {nums[0]*nums[1]}")


with open('2017 input.txt') as file:
    lengths = [ord(i) for i in file.readline()]

suffix = [17, 31, 73, 47, 23]
for i in suffix:
    lengths.append(i)

skipsize = 0
currpos = 0
nums = list(range(256))
for _ in range(64):
    for length in lengths:
        sublist_to_reverse = []
        for i in range(currpos, currpos + length):
            sublist_to_reverse.append(nums[i % len(nums)])
        sublist_to_reverse.reverse()
        for i in range(currpos, currpos + length):
            nums[i % len(nums)] = sublist_to_reverse[i - currpos]

        currpos += length + skipsize
        skipsize += 1


nums = list(batched(nums, 16))

densehash = []
for batch in nums:
    c = batch[0]
    for i in batch[1:]:
        c = c^i

    densehash.append(copy(c))

hexdec = []

for hash in densehash:
    h = hex(hash)[2:]
    while len(h) < 2:
        h = '0'+h

    hexdec.append(copy(h))

print(f'Part 2: {''.join(hexdec)}')