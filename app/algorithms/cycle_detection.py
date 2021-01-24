from typing import List, Dict, Set


def dfs(graph: Dict[str, List[str]], 
        node: str, 
        visited: Dict[str, bool],
        rec_stack: Dict[str, bool]):
    """Performs depth first search on graph"""
    visited[node] = True
    rec_stack[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            if dfs(graph, neighbour, visited, rec_stack):
                return True
        elif rec_stack[neighbour]:
            return True

    rec_stack[node] = False
    return False


def contains_cycle(graph: Dict[str, List[str]]) -> bool:
    """Returns bool if cycle contained in graph"""
    visited = {node: False for node in graph.keys()}
    rec_stack = {node: False for node in graph.keys()}

    for node in graph.keys():
        if visited[node] == False:
            if dfs(graph, node, visited, rec_stack):
                return True
    return False


if __name__ == '__main__':
    graph = {
        'A': ['B', 'D'],
        'B': ['C'],
        'C': [],
        'D': ['C', 'E'],
        'E': ['F'],
        'F': ['D']}

    result = contains_cycle(graph)
    assert result == True 
    print(f'what is the result {result}')
