from copy import deepcopy
from itertools import batched

with open('2021 input') as file:
    lines = [line.strip() for line in file]

nums = list(map(int, lines.pop(0).split(",")))
lines.pop(0)

while '' in lines:
    lines.remove('')


mastercards = list(batched(lines, 5))


for i, card in enumerate(mastercards):
    mastercards[i] = list(card)

for i, card in enumerate(mastercards):
    for y, row in enumerate(card):
        row = row.split(" ")
        while "" in row:
            row.remove("")

        row = list(map(int, row))

        for x, num in enumerate(row):
            row[x] = [num, 0]

        card[y] = row

    mastercards[i] = card

cards = deepcopy(mastercards)

def isBingo(card):
    if any(all(i[1] == 1 for i in row) for row in card):
        total = 0
        for y, row in enumerate(card):
            for x, num in enumerate(row):
                if num[1] == 0:
                    total += num[0]

        return total
    else:
        cols = []
        currcol = []
        for x in range(len(card[0])):
            currcol = []
            for y in range(len(card)):
                currcol.append(card[y][x])

            cols.append(currcol.copy())


        if any(all(i[1] == 1 for i in col) for col in cols):
            total = 0
            for y, row in enumerate(card):
                for x, num in enumerate(row):
                    if num[1] == 0:
                        total += num[0]

            return total

    return -1


z = 0
found = False;
while not found:
    num = nums[z]
    for i, card in enumerate(cards):
        for y, row in enumerate(card):
            for x, n in enumerate(row):
                if n[0] == num:
                    cards[i][y][x][1] = 1


    for card in cards:
        b = isBingo(card)
        if b != -1:
            print(f"Part 1: {b*num}")
            found = True
            break

    z += 1


cards = deepcopy(mastercards)

numWins = 0
z = 0
wins = [0]*len(cards)
found = False
while not found:
    num = nums[z]
    for i, card in enumerate(cards):
        for y, row in enumerate(card):
            for x, n in enumerate(row):
                if n[0] == num:
                    cards[i][y][x][1] = 1


    for l, card in enumerate(cards):
        b = isBingo(card)
        if b != -1:
            if numWins == len(cards)-1 and wins[l] == 0:
                print(f"Part 2: {b * num}")
                found = True
                break
            else:
                if wins[l] == 0:
                    wins[l] = 1
                    numWins += 1

    z += 1

