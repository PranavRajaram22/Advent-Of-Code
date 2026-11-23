from collections import defaultdict
from functools import cache
import statistics

import networkx as nx

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

tree = dict(tree)
children = []
for name in tree.keys():
    for child in tree[name]:
        children.append(child)

for name in names:
    if name not in children:
        root = name
        print(f"Part 1: {root}")

sums = dict()

@cache
def findSum(root):
    try:
        c = 0
        c = weights[root]
        for i in tree[root]:
            c += findSum(i)

        return c
    except KeyError:
        return weights[root]


def rec(root):
    #if it has children
    try:
        children = tree[root]
        children_weights = []
        for child in children:
            children_weights.append(findSum(child))
        mode = statistics.mode(children_weights)
        for i, weight in enumerate(children_weights):
            if weight != mode:
                return rec(children[i])
        return root


    except KeyError:
        return root




unbalanced_node = rec(root)

for node in tree.keys():
    if unbalanced_node in tree[node]:
        children = tree[node]
        children_weights = []
        for child in children:
            children_weights.append(findSum(child))
        mode = statistics.mode(children_weights)
        newweight = mode
        for child in tree[unbalanced_node]:
            newweight -= findSum(child)
        print(f"Part 2: {newweight}")
        break




