from collections import Counter, defaultdict
from copy import deepcopy
from itertools import groupby

mapping = {
    1: 'high card',
    2: "1 pair",
    3: "2 pair",
    4: 'three of a kind',
    5: "fullhouse",
    6: "four of a kind",
    7: "five of a kind"
}
def findType(hand):
    counts = Counter(hand)

    if len(counts.keys()) == 1:
        return 7
    elif len(counts.keys()) == 2:
        for k, v in counts.items():
            if v == 4:
                return 6

        return 5

    else:
        if any(count == 3 for count in counts.values()) and any(count == 2 for count in counts.values()):
            return 5

        elif any(count == 3 for count in counts.values()):
            return 4

        else:
            c = 0
            for count in counts.values():
                if count == 2:
                    c += 1

            if c == 2:
                return 3
            elif c == 1:
                return 2

            else:
                return 1
with open('2023 input') as file:
    lines = [line.strip().split(' ') for line in file]


hands = []
for line in lines:
    hands.append(line[0])

bids = dict()


#1 is a high card
#2 is a 1 pair
#3 is a 2 pair
#4 is a three of a kind
#5 is a fullhouse
#6 is a four of a kind
#7 is a five of a kind






groups = defaultdict(list)
for idx, hand in enumerate(hands):
    hand = list(hand)
    for i, card in enumerate(hand):
        if card == 'T':
            hand[i] = 10
        elif card == 'J':
            hand[i] =  11
        elif card == 'Q':
            hand[i] = 12
        elif card == 'K':
            hand[i] = 13
        elif card == 'A':
            hand[i] = 14
        else:
            hand[i] = int(card)
    groups[findType(hand)].append(hand)
    groups[findType(hand)] = sorted(groups[findType(hand)])
    bids[tuple(hand)] = int(lines[idx][1])



order = []

for i in range(8):
    try:
        hands = groups[i]
        for hand in hands:
            order.append(tuple(hand))

    except ValueError:
        pass


c = 0
for i, hand in enumerate(order):
    c += (i+1) * bids[hand]

print(f"Part 1: {c}")
def findType2(h):
    hand = deepcopy(h)
    numJ = hand.count(1)

    if numJ == 0:
        return findType(hand)
    while hand.count(1) > 0:
        hand.remove(1)

    hand_without_J = hand
    counts = Counter(hand_without_J)
    if numJ == 4 or numJ == 5:
        return 7

    elif numJ == 3:
        if any(i == 2 for i in counts.values()):
            return 7
        else:
            return 6

    elif numJ == 2:
        if any(i == 3 for i in counts.values()):
            return 7
        elif any(i == 2 for i in counts.values()):
            return 6
        else:
            return 4

    elif numJ == 1:
        if any(i == 4 for i in counts.values()):
            return 7
        elif any(i == 3 for i in counts.values()):
            return 6
        elif any(i == 2 for i in counts.values()):
            c = 0
            for count in counts.values():
                if count == 2:
                    c += 1

            if c == 1:
                return 4
            elif c == 2:
                return 5

        else:
            return 2

    return 1


with open('2023 input') as file:
    lines = [line.strip().split(' ') for line in file]


hands = []
for line in lines:
    hands.append(line[0])

bids = dict()
groups = defaultdict(list)
for idx, hand in enumerate(hands):
    hand = list(hand)
    for i, card in enumerate(hand):
        if card == 'T':
            hand[i] = 10
        elif card == 'J':
            hand[i] =  1
        elif card == 'Q':
            hand[i] = 12
        elif card == 'K':
            hand[i] = 13
        elif card == 'A':
            hand[i] = 14
        else:
            hand[i] = int(card)

    groups[findType2(hand)].append(hand)
    groups[findType2(hand)] = sorted(groups[findType2(hand)])
    bids[tuple(hand)] = int(lines[idx][1])

order = []
for i in range(1,8):
    hands = groups[i]
    for hand in hands:
        order.append(tuple(hand))
c = 0
for i, hand in enumerate(order):
    c += (i+1) * bids[hand]

print(f"Part 2: {c}")