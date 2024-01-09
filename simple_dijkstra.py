import math
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
    'A': {'B': 2, 'G': 3},
    'B': {'A': 2, 'H': 2},
    'C': {'D': 3, 'G': 1},
    'D': {'C': 3, 'H': 2, 'I': 2},
    'G': {'A': 3, 'C': 1, 'K': 3, 'L': 1},
    'H': {'B': 2, 'D': 2, 'L': 4},
    'I': {'D': 2, 'M': 3},
    'K': {'G': 3},
    'L': {'G': 1, 'H': 4, 'M': 2},
    'M': {'I': 3, 'L': 2}
}

G = networkx.Graph()

G.add_nodes_from(example_adj_dict.keys())
G.add_weighted_edges_from(
    [
        (start, finish, example_adj_dict[start][finish]) for start in example_adj_dict for finish in example_adj_dict[start]
    ]
)

pos = networkx.spring_layout(G)
labels = networkx.get_edge_attributes(G, 'weight')

networkx.draw_networkx(G, pos)
networkx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

while True:
    start = input('Where to start? ')

    queue = [start]

    distances = {node: math.inf for node in example_adj_dict}
    distances[start] = 0

    traversal = []

    while queue:
        print(queue)
        node = min(queue, key=lambda n: distances[n])
        queue.remove(node)

        traversal.append(node)

        for neighbour in example_adj_dict[node]:
            new_dist = distances[node] + example_adj_dict[node][neighbour]
            if new_dist < distances[neighbour]:
                distances[neighbour] = new_dist

                queue.append(neighbour)

    print(f'Traversal starting at {start}: {traversal}')
