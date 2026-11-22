from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd

with open('2024 input') as file:
    grid = [list(line.strip()) for line in file]


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

df = pd.DataFrame(grid)
print(df)
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 0:
            visited = []
            adj = []
            dfs(x, y, 0, visited, adj)
            print(adj)
            G = nx.DiGraph(adj)

            H = deepcopy(G)
            indegrees = dict(H.in_degree())
            queue = []
            order = []

            for node, count in indegrees.items():
                if count == 0:
                    queue.append(node)
                    H.remove_node(node)


            while queue:
                print(f"Nodes: {H.nodes()}")
                print(f"Queue: {queue}")
                print(f"Indegrees {indegrees}")
                print("______")
                print("")

                while queue:
                    node = queue.pop()
                    order.append(node)
                    if node in H.nodes():
                        print("removing", node)
                        H.remove_node(node)
                indegrees = dict(H.in_degree())
                for node, count in indegrees.items():
                    if count == 0:
                        queue.append(node)

            print(order)


            pos = {n: (n[0], -n[1]) for n in G.nodes()}

            nx.draw(G, pos, arrows=True, with_labels=True)
            plt.show()


            for coord in visited:
                if grid[coord[1]][coord[0]] == 9:
                    c += 1


print(f'Part 1: {c}')

