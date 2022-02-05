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


if __name__ == '__main__':
    res = pascals_triangle(4)
    expected = [1, 4, 6, 4, 1]
    print(f'res {res}')
    assert res == expected 
