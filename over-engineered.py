from dataclasses import dataclass, field
import random as r

@dataclass
class Node:
    label: [str | None] = None
    value: object = None
    visited: bool = False

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def is_visited(self) -> bool:
        return self.visited


@dataclass
class Edge:
    start: Node
    finish: Node
    label: str = None
    value: int = None
    directed: bool = False

    def start(self) -> Node:
        return self.start

    def finish(self) -> Node:
        return self.finish

    def is_directed(self) -> bool:
        return self.directed

    def reversed(self) -> 'Edge':
        return Edge(
            start=self.finish,
            finish=self.start,
            label=f'reversed {self.label}',
            value=self.value
        )

@dataclass
class Traversal:
    node_dict: {Node} = field(default_factory=dict)

    def add_node(self, node: Node, predecessor: Node | None = None):
        self.node_dict[node] = predecessor

    def get_journey(self, target: Node):
        if target not in self.node_dict:
            return []
        else:
            cursor = target
            journey: [Node] = []
            while cursor:
                journey.append(cursor)
                cursor = self.node_dict[cursor]
                

class Graph:
    def __init__(self,
                 node_list: [Node] = None,
                 edge_list: [(Node, Node)] = None
                 ):
        self.node_list: dict = dict()
        self.cycles_checked: bool = False
        self.has_cycles: bool | None = None

        for node in node_list:
            self.add_node(node)

        for edge in edge_list:
            self.add_edge(edge)

    def add_node(self, node: Node):
        if node not in self.node_list:
            self.node_list[node] = {}

    def add_edge(self, edge: Edge):
        self.add_node(edge.start())
        self.add_node(edge.finish())

        self.node_list[edge.start()][edge.finish()] = edge

        if edge.is_directed():
            self.node_list[edge.finish()][edge.start()] = edge.reversed()

    def get_neighbours(self, node: Node) -> {Node: Edge}:
        if node in self.node_list:
            return self.node_list[node]
        else:
            return dict()

    def mark_all_unvisited(self):
        map(Node.mark_unvisited, self.node_list)

    def traverse(
            self,
            start_node: Node,
            target_node: Node | None = None
    ) -> (Traversal, bool):
        self.mark_all_unvisited()

        the_traversal: [Node] = []
        found_target = False
        cycle_check: bool = False
        traversal_stack: [Node] = [start_node]

        while traversal_stack:
            node = traversal_stack.pop()
            the_traversal.append(node)
            node.mark_visited()

            if node is target_node:
                found_target  = True
                break

            for neighbour in self.get_neighbours(node):
                if neighbour.is_visited():
                    cycle_check = True
                else:
                    traversal_stack.append(neighbour)

        self.cycles_checked = True
        self.has_cycles = cycle_check

        return the_traversal, found_target



num_nodes = 20
num_sides = 10

nodes = [Node() for i in range(num_nodes)]
print(nodes)
print(r.sample(nodes, 2))

sides = [Edge(A, B) for [A, B] in tuple(r.sample(nodes, 2))]

G = Graph(nodes, sides)

T = G.traverse(nodes[0])
