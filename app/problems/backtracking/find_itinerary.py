from collections import defaultdict


def build_graph(tickets):
    graph = defaultdict(list)

    for origin, dest in tickets:
        graph[origin].append(dest)

    return graph


def find_itinerary(tickets):
    graph = build_graph(tickets)
    visited = dict()
    ans = []

    for origin, dests in graph.items():
        graph[origin].sort()
        visited[origin] = [False] * len(dests)

    def backtrack(loc, path):
        nonlocal ans

        if len(path) == len(tickets) + 1:
            ans = path
            return True

        for i, next_loc in enumerate(graph[loc]):
            if not visited[loc][i]:
                visited[loc][i] = True
                ret = backtrack(next_loc, path + [next_loc])
                if ret:
                    return True
                else:
                    visited[loc][i] = False
        return False

    backtrack('JFK', ['JFK'])
    return ans


if __name__ == '__main__':
    tickets = [
        ["EZE", "TIA"],
        ["EZE", "AXA"],
        ["AUA", "EZE"],
        ["EZE", "JFK"],
        ["JFK", "ANU"],
        ["JFK", "ANU"],
        ["AXA", "TIA"],
        ["JFK", "AUA"],
        ["TIA", "JFK"],
        ["ANU", "EZE"],
        ["ANU", "EZE"],
        ["TIA", "AUA"]]

    result = find_itinerary(tickets)
    print(f'result -> {result}')
