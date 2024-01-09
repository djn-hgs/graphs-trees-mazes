import random
import matplotlib.pyplot as plt
import string as s

import networkx


def my_adj_dict(num_nodes=15, num_edges=20):

    adj_dict: dict[str, dict[str, dict]] = {}

    for i in range(num_nodes):
        new_node = s.ascii_uppercase[i]
        adj_dict[new_node] = {}

    for j in range(num_edges):
        start: str = random.choice(list(adj_dict))
        finish: str = random.choice(list(adj_dict))

        adj_dict[start][finish] = {'directed': False}
        adj_dict[finish][start] = {'directed': False}

    return adj_dict


example_adj_dict = {
    'A': ['B', 'G'],
    'B': ['A', 'H'],
    'C': ['D', 'G'],
    'G': ['A', 'C', 'K', 'L'],
    'D': ['C', 'H', 'I'],
    'H': ['B', 'D', 'L'],
    'I': ['D', 'M'],
    'K': ['G'],
    'L': ['G', 'H', 'M'],
    'M': ['I', 'L']
}


G = networkx.Graph()

G.add_nodes_from(example_adj_dict.keys())
G.add_edges_from(
    [
        (start, finish) for start in example_adj_dict for finish in example_adj_dict[start]
    ]
)

networkx.draw_networkx(G)

plt.show()

while True:
    start = input(f'Where to start? ')

    queue = [start]
    visited = [start]
    traversal = []

    while queue:
        node = queue.pop(0)

        traversal.append(node)

        for neighbour in example_adj_dict[node]:
            if neighbour not in visited:
                visited.append(neighbour)

                queue.append(neighbour)

    print(f'Traversal starting at {start}: {traversal}')

