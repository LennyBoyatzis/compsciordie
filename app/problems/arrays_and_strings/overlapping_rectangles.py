def calc_unit_recs(rectangle):
    rectangle.sort()
    bottom_left, top_left, bottom_right, top_right = rectangle
    units = []

    for y in range(bottom_left[1] + 1, top_left[1] + 1):
        for x in range(top_left[0] + 1, top_right[0] + 1):
            units.append((x, y))

    return units


def get_overlap_area(rectangles):
    top_rights = set()
    used_top_rights = set()
    area = 0
    
    for rect in rectangles:
        unit_top_rights = calc_unit_recs(rect)

        for top_right in unit_top_rights:
            if top_right in top_rights:
                if top_right not in used_top_rights:
                    area += 1
                    used_top_rights.add(top_right)
            else:
                top_rights.add(top_right)

    return area


if __name__ == '__main__':
    """
    Sorting Tuples in Python (Default Behaviour)
    - It will automatically sort a list of tuples by the first element in the
    tuples, then by the second elements and so on.
    """
    rectangles = [
        [(1,1), (1,2), (2,1), (2,2)],
        [(2,3), (2,6), (5,3), (5,6)],
        [(4,2), (4,5), (7,2), (7,5)],
        [(4,3), (4,4), (5,3), (5,4)],
        [(6,6), (6,7), (7,6), (7,7)]]

    res = get_overlap_area(rectangles)
    print(f'res {res}')
    assert res == 2

    rectangles = [
        [(1,1), (1,2), (2,1), (2,2)],
        [(2,3), (2,6), (5,3), (5,6)],
        [(4,2), (4,5), (7,2), (7,5)],
        [(4,3), (4,4), (5,3), (5,4)],
        [(6,6), (6,7), (7,6), (7,7)],
        [(6,1), (8,1), (6,8), (8,8)]]

    res = get_overlap_area(rectangles)
    print(f'res {res}')
    assert res == 6 
