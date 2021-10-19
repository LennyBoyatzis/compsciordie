def get_diagonals(p1, p2):
    x_1, y_1 = p1
    x_2, y_2 = p2

    return (x_1, y_2), (x_2, y_1)


def min_area_rectangle(points):
    min_area = float('inf')
    points_set = set([tuple(point) for point in points])

    for i in range(len(points)):
        for j in range(i):
            p1 = points[i]
            p2 = points[j]
            x_1, y_1 = p1
            x_2, y_2 = p2
            if x_1 != x_2 and y_1 != y_2:
                diagonals = get_diagonals(p1, p2)
                if diagonals[0] in points_set and diagonals[1] in points_set:
                    min_area = min(min_area, abs(x_1 - x_2) * abs(y_1 - y_2))
    return min_area if min_area != float('inf') else 0


if __name__ == '__main__':
    points = [
        [1, 5],
        [5, 1],
        [4, 2],
        [2, 4],
        [2, 2],
        [1, 2],
        [4, 5],
        [2, 5],
        [-1, -2]
    ]

    ans = min_area_rectangle(points)
    print(ans)
