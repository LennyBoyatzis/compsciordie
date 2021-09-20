def get_prev_smaller_idx(array, i):
    for j in range(i, -1, -1):
        if array[j] < array[i]:
            return j
    return i


def get_max_subsequence(array, i):
    indices = [i]
    prev_val = array[i]

    for j in range(i, -1, -1):
        if array[j] < prev_val:
            indices.append(j)
            prev_val = array[j]

    print(f'indices {indices}')
    return [array[i] for i in indices[::-1]]


def max_sum_inc_sub(array):
    size = len(array)
    sums = [0] * size
    sums[0] = array[0]

    for i in range(1, size):
        num = array[i]
        prev_num_idx = get_prev_smaller_idx(array, i)
        sums[i] = num + sums[prev_num_idx]

    max_sum = max(sums)
    max_index = sums.index(max_sum)

    print(f'max_sum {max_sum}')
    print(f'max_index {max_index}')

    max_subsequence = get_max_subsequence(array, max_index)

    return [max_sum, max_subsequence]


if __name__ == '__main__':
    array = [10, 70, 20, 30, 50, 11, 30]
    res = max_sum_inc_sub(array)
    print(f'res {res}')
