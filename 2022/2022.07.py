from functools import cache

import networkx as nx
import matplotlib.pyplot as plt

with open('2022 input') as file:
    lines = [line.strip() for line in file]


# Create a directed graph
G = nx.DiGraph()


# Draw the tree using hierarchical layout
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, arrows=False, node_color="lightblue", node_size=1500)
plt.show()


