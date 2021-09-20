def search_left_bound(array, target):
    left, right = 0, len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] >= target:
            right = mid
        else:
            left = mid + 1

    if array[left] == target:
        return left
    else:
        return -1

def search_right_bound(array, target):
    left, right = 0, len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] > target:
            right = mid
        else:
            left = mid + 1

    if array[left-1] == target:
        return left-1 
    else:
        return -1


def search_for_range(array, target):
    left_index = search_left_bound(array, target)
    right_index = search_right_bound(array, target)

    return [left_index, right_index]


if __name__ == '__main__':
    array = [5, 7, 7, 8, 8, 8, 10]
    target = 8 
    res = search_for_range(array, target)
    print(f'res {res}')
