import math


def get_distance_from_origin(coords):
    a, b = coords
    return math.sqrt(a**2 + b**2)


def find_k_closest_points_to_origin(points, K):
    return sorted(points, key=lambda point: get_distance_from_origin(point))[:K]


if __name__ == '__main__':
    K = 2
    points = [
        [3, 3],
        [5, -1],
        [-2, 4]]
    result = find_k_closest_points_to_origin(points, K)
    print(f'result {result}')
