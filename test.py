from collections import defaultdict, deque


def top_sort(dependencies, n):
    graph = defaultdict(list)
    in_edges_counts = {str(i): 0 for i in range(1, n+1)}

    # Build graph & in_edges counter
    for p1, p2 in dependencies:
        graph[p1].append(p2)
        in_edges_counts[p2] += 1

    zero_edge_nodes = []

    # Find nodes with zero incoming edges
    for edge, count in in_edges_counts.items():
        if count == 0:
            zero_edge_nodes.append(edge)

    top_order = []

    # Keep exploring and removing nodes
    while zero_edge_nodes:
        node = zero_edge_nodes.pop()
        top_order.append(node)

        for neighbour in graph[node]:
            in_edges_counts[neighbour] -= 1

            if in_edges_counts[neighbour] == 0:
                zero_edge_nodes.append(neighbour)

    return top_order


if __name__ == '__main__':
    dependencies = [
        ['1', '2'],
        ['2', '4'],
        ['3', '4'],
        ['4', '5'],
        ['4', '6'],
        ['5', '7']]

    n = 7
    ans = top_sort(dependencies, n)
    print(f'ans {ans}')
