def get_overlap_area(rectangles):
    pass

if __name__ == '__main__':
    rectangles = [
        [(1,1), (1,2), (2,1), (2,2)],
        [(2,3), (2,6), (5,3), (5,6)],
        [(4,2), (4,5), (7,2), (7,5)],
        [(4,3), (4,4), (5,3), (5,4)],
        [(6,6), (6,7), (7,6), (7,7)]
    ]

    res = get_overlap_area(rectangles)
    print(f'res {res}')
