def relative_sort_order(A, B):
    pass


if __name__ == '__main__':
    A = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    B = [2, 1, 4, 3, 9, 6]
    ans = relative_sort_order(A, B)
    expected = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    assert expected == ans
    print(f'ans {ans}')
