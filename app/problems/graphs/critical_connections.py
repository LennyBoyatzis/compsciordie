from collections import defaultdict


def make_graph(connections):
    graph = defaultdict(list)

    for conn in connections:
        node1, node2 = conn
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph


def dfs(graph):
    visited = set([])

    def search(node):
        if node not in visited:
            children = graph[node]
            visited.add(node)

            for child in children:
                if child not in visited:
                    return search(child)
        return

    search(0)
    print(f'what is visited {visited}')


"""
An edge is a critical connection if it is not in a cycle
Steps:
    - Discard all edges in cycles
    - Remaining connections are a complete collection of critical connections
"""


def critical_connections(n, connections):
    graph = make_graph(connections)
    dfs(graph)


if __name__ == '__main__':
    n = 6
    connections = [
        [0, 1],
        [1, 2],
        [2, 0],
        [1, 3],
        [3, 4],
        [4, 5],
        [5, 3]]
    result = critical_connections(n, connections)
    print(f'result {result}')
