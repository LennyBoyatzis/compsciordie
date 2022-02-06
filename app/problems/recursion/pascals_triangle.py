def pascals_triangle(row_index):
    """Returns row in pascals triangle corresponding to parameter"""
    if row_index == 0:
        return [1]
    else:
        prev_line = pascals_triangle(row_index - 1)
        line = [1]

        for i in range(len(prev_line) -1):
            line.append(prev_line[i] + prev_line[i+1])

        line += [1]

        return line


def get_num(row, col):
    if row == 0 or col == 0 or row == col:
        return 1
    return get_num(row-1, col-1) + get_num(row-1, col)


def pascals_triangle_brute_force(row_index):
    ans = []

    for col in range(row_index):
        ans.append(get_num(row_index, col))

    return ans

    


if __name__ == '__main__':
    res = pascals_triangle(4)
    expected = [1, 4, 6, 4, 1]
    print(f'res {res}')
    assert res == expected 
