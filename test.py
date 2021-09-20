
def binary_search(array):
    left, right = 0, len(array) - 1

    while left < right:
        mid = (left + right) // 2

        if array[mid] > array[mid+1]:
            right = mid
        else:
            left = mid + 1

    return right


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    res = binary_search(array)
    print(f'res {res}')
