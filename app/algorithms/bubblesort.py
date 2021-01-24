def bubblesort(array):
    size = len(array)

    for i in range(size):
        for j in range(i+1, size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


if __name__ == '__main__':
    array = [1, 9, 12, 3, 4, 20, -10]
    result = bubblesort(array)
    print(f'result {result}')
