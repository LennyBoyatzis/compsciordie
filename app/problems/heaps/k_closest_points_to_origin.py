import math
import heapq

"""
Keep a min heap of size k
- For each item, insert into heap
- If inserting an item, makes heap size larger than k, then we immediately pop after inserting (heappushpop)

k - number of closest elements
n - number of points

Complexities:
    time:
        inserting into heap O(log(k))
        for each item point O(nlog(k))
    space:
        heap: O(k)
"""


def find_k_closest_points_to_origin(points, K):
    heap = []

    for (x, y) in points:
        dist = abs(math.sqrt(x**2 + y**2))

        if len(heap) == K:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))

    return [[x, y] for (dist, x, y) in heap]


if __name__ == '__main__':
    K = 2
    points = [
        [3, 3],
        [5, -1],
        [-2, 4]]
    result = find_k_closest_points_to_origin(points, K)
    print(f'result {result}')
