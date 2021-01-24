from typing import List, Dict
from collections import defaultdict


def top_sort(graph: Dict[str, List[str]]) -> List[str]:
    """Returns topological ordering of a graph"""
    in_graph = defaultdict(int)

    # Sum incoming edges for each node
    for node in graph.keys():
        neighbours = graph[node]

        for neighbour in neighbours:
            in_graph[neighbour] += 1

    zero_in_edges = []

    # Find nodes with zero incoming edges
    for node in graph.keys():
        if node not in in_graph:
            zero_in_edges.append(node)

    top_order = []

    # Keep exploring and removing nodes
    while len(zero_in_edges) > 0:
        node = zero_in_edges.pop()
        top_order.append(node)

        for neighbour in graph[node]:
            in_graph[neighbour] -= 1
            if in_graph[neighbour] == 0:
                zero_in_edges.append(neighbour)

    return top_order


if __name__ == '__main__':
    graph = {
        'B': ['E', 'C'],
        'E': ['A', 'C'],
        'C': ['D'],
        'A': ['C', 'D'],
        'D': []}

    result = top_sort(graph)
    assert result == ['B', 'E', 'A', 'C', 'D']
    print(f'what is the result {result}')
