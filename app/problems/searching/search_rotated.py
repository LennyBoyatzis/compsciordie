def find_rotation(array):
    left, right = 0, len(array) - 1

    while left < right:
        mid = (left + right) // 2

        if array[left] < array[mid]:
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    array = [21, 22]
    # array = [6, 7, 8, 9, 10]
    res = find_rotation(array)
    print(f'res {res}')
