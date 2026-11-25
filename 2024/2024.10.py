from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

import pandas as pd

with open('2024 input') as file:
    grid:list = [list(line.strip()) for line in file]


for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == '.':
            grid[y][x] = '100'


for y, line in enumerate(grid):
    grid[y] = list(map(int, line))



def dfs(x, y, num, visited, adj):
    visited.append((x, y))
    adjcoords = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
    if grid[y][x] == 9:
        return visited
    for a in adjcoords:
        xi, yi = a
        if 0 <= xi < len(grid[0]) and 0 <= yi < len(grid) and grid[yi][xi] == num+1:
            if (xi, yi) not in visited:
                dfs(xi, yi, num + 1, visited, adj)
                adj.append([(x, y), (xi, yi)])
            else:
                if [(x, y), (xi, yi)] not in adj:
                    adj.append([(x, y), (xi, yi)])

c = 0
c2 = 0
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        visited = []
        adj = []
        if char == 0:
            dfs(x, y, 0, visited, adj)

            c += len([i for i in visited if grid[i[1]][i[0]] == 9])

            graph = defaultdict(list)

            for pair in adj:
                graph[pair[0]].append(pair[1]) #graph[pointer] = pointed



            G = nx.DiGraph(adj)
            # only for drawing
            '''
            pos = {n: (n[0], -n[1]) for n in G.nodes()}
            nx.draw(G, pos, with_labels=True)
            plt.show()
            '''
            #

            topsort = list(nx.topological_sort(G))
            dp = defaultdict(int)
            dp[topsort[0]] = 1
            for u in topsort:
                for v in graph[u]:
                    dp[v] += dp[u]
            for v in topsort:
                if grid[v[1]][v[0]] == 9:
                    c2 += dp[v]




print(f'Part 1: {c}')
print(f"Part 2: {c2}")
