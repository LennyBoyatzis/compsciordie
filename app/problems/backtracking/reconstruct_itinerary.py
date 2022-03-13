from collections import defaultdict


def build_graph(tickets):
    graph = defaultdict(list)
    
    for fro, to in tickets:
        graph[fro].append(to)
        
    for k, v in graph.items():
        v.sort(reverse=True)
    
    return graph
    
            
def find_itinerary(tickets):
    graph = build_graph(tickets)
    num_trips = len(tickets)
    ans = []
    
    def backtrack(path, graph):
        # Found valid path
        if len(path) - 1 == num_trips:
            # Make sure you append a copy of the path
            ans.append(path[:])
            return
        
        # Get current city
        curr_city = path[-1]
        
        # Get candidate paths
        candidates = graph[curr_city]

        for i in range(len(candidates)):
            # Explore next city
            next_city = graph[curr_city].pop()
            print(f'graph {graph}')
            path.append(next_city)
            backtrack(path, graph)

            # Remove next city from path and 
            graph[curr_city].append(next_city)
            path.pop()
            
            
    backtrack(['JFK'], graph)
    return ans
    # return ans[0]


if __name__ == '__main__':
    tickets = [
        ["JFK","KUL"],
        ["JFK","NRT"],
        ["NRT","JFK"]
    ]
    result = find_itinerary(tickets)
    print(f'result -> {result}')


    # tickets = [
    #     ["EZE", "TIA"],
    #     ["EZE", "AXA"],
    #     ["AUA", "EZE"],
    #     ["EZE", "JFK"],
    #     ["JFK", "ANU"],
    #     ["JFK", "ANU"],
    #     ["AXA", "TIA"],
    #     ["JFK", "AUA"],
    #     ["TIA", "JFK"],
    #     ["ANU", "EZE"],
    #     ["ANU", "EZE"],
    #     ["TIA", "AUA"]]

    # result = find_itinerary(tickets)
    # print(f'result -> {result}')
