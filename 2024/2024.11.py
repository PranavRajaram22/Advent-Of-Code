from collections import defaultdict
from copy import copy


for blinks in [25, 75]:
    with open('2024 input') as file:
        start = list(map(int, file.readline().strip().split(' ')))

    stones = defaultdict(int)

    for startstone in start:
        stones[startstone] += 1


    for _ in range(blinks):

        newstones = defaultdict(int)

        for stone, count in stones.items():
            if stone == 0:
                newstones[1] += count
            elif len(str(stone))%2 == 0:
                firsthalf, secondhalf = divmod(stone, 10**(len(str(stone))//2))
                newstones[firsthalf] += count
                newstones[secondhalf] += count

            else:
                newstones[stone*2024] += count

        stones = copy(newstones)


    if blinks == 25:
        print(f"Part 1: {sum(stones.values())}")

    else:
        print(f"Part 2: {sum(stones.values())}")
