from collections import defaultdict

with open('2017 input.txt') as file:
    lines = [line.strip() for line in file]

tree = defaultdict(list)
weights = dict()
names = []
for line in lines:
    line = line.split(" ")
    name = line[0]
    names.append(name)
    weight = int(line[1][1:-1])
    weights[name] = weight
    if len(line) > 2: #has children
        for i in range(line.index("->")+1, len(line)):
            if i != len(line)-1:
                tree[name].append(line[i][:-1])
            else:
                tree[name].append(line[i])


children = []
for name in tree.keys():
    for child in tree[name]:
        children.append(child)

for name in names:
    if name not in children:
        root = name
        print(f"Part 1: {root}")

def rec(root):
    children = tree[root]
    print(root)


print(rec(root))