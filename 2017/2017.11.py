with open('2017 input.txt') as file:
    steps = file.readline().split(",")

print(steps)

n, ne, nw = 0, 0, 0

for step in steps:
    if step == 'n':
        n += 1
    elif step == 's':
        n -= 1

    elif step == 'ne':
        ne += 1
    elif step == 'sw':
        ne -= 1

    elif step == 'nw':
        nw += 1
    elif step == 'se':
        nw -= 1


def sign(x):
    if x < 0:
        return "-"
    else:
        return '+'

print(n, ne, nw)
while True:
    if any(i == 0 for i in [n, ne, nw]):
        print(abs(n) + abs(ne) + abs(nw))
        break
    if all(i > 0 for i in [n, ne, nw]) or all(i < 0 for i in [n, ne, nw]):
        print((abs(n) + abs(ne) + abs(nw)))
    if n <= ne and n <= nw:
        if ne > 0 and nw > 0:
            n += 1
            ne -= 1
            nw -= 1
        elif ne < 0 and nw < 0:
            n -= 1
            ne += 1
            nw += 1