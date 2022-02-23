import math
import heapq

def get_neighbours(p1):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    neighbours = []

    for x_off, y_off in directions:
        new_point = [p1[0] + x_off, p1[1] + y_off]
        neighbours.append(new_point)

    return neighbours


def calc_euclidean_distance(p1, p2):
    return math.sqrt(sum([(a - b)**2 for a, b in zip(p1, p2)]))


class HeapNode:
    def __init__(self, point, distance=0, time=0):
        self.point = point
        self.distance = distance
        self.time = time 

    def __lt__(self, val):
        return self.distance < val

    def __gt__(self, val):
        return self.distance > val


def find_shortest_path(p1, p2):
    start_dist = calc_euclidean_distance(p1, p2)
    pq = [HeapNode(p1, start_dist, 0)]

    while pq:
        node = heapq.heappop(pq)
        neighbours = get_neighbours(node.point)

        if node.point == p2:
            return node.time

        for neighbour in neighbours:
            neighbour_dist = calc_euclidean_distance(neighbour, p2)
            if neighbour_dist <= node.distance:
                new_node = HeapNode(neighbour, neighbour_dist, node.time+1)
                heapq.heappush(pq, new_node)


def min_time_to_visit_all_points(points):
    total_time = 0

    for i in range(1, len(points)):
        total_time += find_shortest_path(points[i-1], points[i])

    return total_time

if __name__ == '__main__':
    points = [[1, 1], [3, 4], [-1, 0]]
    ans = min_time_to_visit_all_points(points)
