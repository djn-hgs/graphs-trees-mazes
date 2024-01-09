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
    start = input(f'Where to start? ')

    queue = [start]
    visited = [start]
    traversal = []

    distance = {
        node: math.inf for node in example_adj_dict
    }

    distance[start] = 0

    while queue:
        node = queue.pop(0)

        traversal.append(node)

        print(f'Visiting {node}')
        print(f'Queue {queue}')

        for neighbour in example_adj_dict[node]:
            print(f'Neighbour {neighbour}')

            new_dist = distance[node] + example_adj_dict[node][neighbour]

            if new_dist < distance[neighbour]:
                visited.append(neighbour)

                distance[neighbour] = new_dist

                queue.append(neighbour)

            print(f'Distances {distance}')

    print(f'Traversal starting at {start}: {traversal}')
