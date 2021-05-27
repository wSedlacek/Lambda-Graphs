from typing import List, Tuple
from util import Queue


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node: int):
        self.nodes[node] = set()

    def add_edge(self, edge: Tuple[int]):
        for node in edge:
            if node not in self.nodes:
                self.add_node(node)

        self.nodes[edge[1]].add(edge[0])

    def get_neighbors(self, node_id: int):
        if node_id in self.nodes:
            return self.nodes[node_id]
        else:
            raise ValueError("This node does not exist...")

    def longest_path(self, starting_node: int):
        queue = Queue()
        queue.push([starting_node])
        visited = {starting_node}
        longest_path = []

        while not queue.empty():
            path = queue.pop()
            node = path[-1]
            longest_path = longest_path if len(longest_path) > len(path) else path
            for next_node in self.get_neighbors(node):
                if next_node not in visited:
                    visited.add(next_node)
                    queue.push([*path, next_node])

        return longest_path


def earliest_ancestor(ancestors: List[Tuple[int]], starting_node: int):
    """
    Finds the earliest ancestor of a given ancestor graph.

    Returns -1 if an ancestor is not found
    """

    graph = Graph()

    for edge in ancestors:
        graph.add_edge(edge)

    path = graph.longest_path(starting_node)

    if len(path) < 2:
        return -1
    else:
        return path[-1]
