from math import floor

with open('2023 input') as file:
    cards = [card.strip() for card in file]

def check(card, part1):
    card = card.split(":")

    card[1] = card[1].split(" | ")
    card[0] = int(card[0].split(" ")[-1])
    winnums, nums = card[1]

    winnums = winnums.split(" ")
    while "" in winnums:
        winnums.remove("")
    winnums = list(map(int, winnums))

    nums = nums.split(" ")
    while "" in nums:
        nums.remove("")
    nums = list(map(int, nums))
    e = 0
    for i in nums:
        if i in winnums:
            e += 1
    if part1:
        return floor(2 ** (e - 1))
    else:
        return e


total = 0
for card in cards:
    total += check(card, 1)

print(f"Part 1: {total}")
numcards = dict()

lencards = len(cards)

for i in range(1, lencards+1):
    numcards[i] = 1

for i, card in enumerate(cards):
    t = check(card, part1=False)
    for x in range(i+2, i+t+2):
        numcards[x] += numcards[i+1]


print(f'Part 2: {sum(numcards.values())}')



