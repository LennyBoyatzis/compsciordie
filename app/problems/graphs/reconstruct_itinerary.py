import heapq
from collections import defaultdict


def build_graph(tickets):
    graph = defaultdict(list)

    for (origin, dest) in tickets:
        heapq.heappush(graph[origin], dest)

    return graph


def find_itinerary(tickets):
    """
    Maintain a set of tuples
    trips = set([
        ('MUC', 'LHR'),
        ('JFK', 'MUC'),
        ('SFO', 'SJC'),
        ('LHR', 'SFO')])

    graph = {
        'MUC': ['LHR'],
        'JFK': ['MUC'],
        'SFO': ['ALR', 'SJC'],
        'SJC': ['SFO'],
        'LHR': ['SFO']}

    result = [
        ['JFK', 'MUC'],
        ['MUC', 'LHR'],
        ['LHR', 'SFO'],
        ['SFO', 'ALR']]

    should be

    result = [
        ['JFK', 'MUC'],
        ['MUC', 'LHR'],
        ['LHR', 'SFO'],
        ['SFO', 'SJC'],
        ['SJC', 'SFO'],
        ['SFO', 'ALR']]


    """
    graph = build_graph(tickets)

    def search(origin, trips=set(), itinerary=[]):
        dests = graph[origin]

        for dest in dests:
            trip = (origin, dest)

            if trip not in trips:
                trips.add(trip)
                itinerary.append([origin, dest])
                search(dest, trips, itinerary)
            return itinerary

    return search('JFK')


if __name__ == '__main__':
    tickets = [
        ["MUC", "LHR"],
        ["JFK", "MUC"],
        ["SFO", "SJC"],
        ["LHR", "SFO"]]

    tickets_2 = [
        ["MUC", "LHR"],
        ["JFK", "MUC"],
        ["SFO", "SJC"],
        ["SJC", "SFO"],
        ["SFO", "ALR"],
        ["LHR", "SFO"]]

    result = find_itinerary(tickets_2)
    print(f'what is the xxx {result}')
