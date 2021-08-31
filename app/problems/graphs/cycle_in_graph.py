from typing import List, Dict

from collections import defaultdict

Edges = List[int]
Graph = Dict[int, Edges]

def build_graph(edges: List[Edges]) -> Graph:
    graph = defaultdict(list)

    for node, edges in enumerate(edges):
        graph[node].extend(edges)

    return graph

def dfs(node, graph, visited, instack):
    if node:
        descendants = graph[node]
        for desc in descendants:
            if desc not in visited:
                instack.append(node)
                dfs(node, graph, visited, instack)
                instack.pop()
    



def find_cycle(edges: List[Edges]) -> bool:
    visited = set()
    graph = build_graph(edges)




if __name__ == '__main__':
    adjacency_list = [
        [1, 3],
        [2, 3, 4],
        [0],
        [],
        [2, 5],
        []]

    # graph = build_graph(adjacency_list)
    # print(f'graph {graph}')

    has_cycle = find_cycle(adjacency_list)
    print(f'contains_cycle {contains_cycle}')
