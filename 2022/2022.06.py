from collections import deque
from itertools import islice


def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 3) → ABC BCD CDE DEF EFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)




def process(string):
    windows = list(sliding_window(string, 4))
    for i, tup in enumerate(windows):
        if all(tup.count(k) == 1 for k in tup):
            return i+4


with open('2022 input') as file:
    lines = [line.strip() for line in file]

total = sum([process(i) for i in lines])

print(total)

def process2(string):
    windows = list(sliding_window(string, 14))
    for i, tup in enumerate(windows):
        if all(tup.count(k) == 1 for k in tup):
            return i + 14

total = sum([process2(i) for i in lines])
print(total)