def selection_sort(array):
    size = len(array)
    next_idx = size - 1

    while next_idx > 0:
        for i in range(next_idx):
            if array[i] > array[next_idx]:
                array[next_idx], array[i] = array[i], array[next_idx]

        next_idx -= 1
    return array


if __name__ == '__main__':
    array = [1, 9, 12, 3, 4, 20, -10]
    result = selection_sort(array)
    print(f'result {result}')
