def get_sequence(array, sequences, curr_idx):
    sequence = []

    while curr_idx:
        sequence.append(array[curr_idx])
        curr_idx = sequences[curr_idx]

    return list(reversed(sequence))
        
def max_sum_inc_sub(array):
    size = len(array)
    sequences = [None for num in array]
    sums = [num for num in array]
    max_idx = 0

    for i in range(size):
        curr = array[i]
        for j in range(0, i):
            prev = array[j]
            if prev < curr and sums[j] + curr >= sums[i]:
                sums[i] = sums[j] + curr
                sequences[i] = j
        if sums[i] >= sums[max_idx]:
            max_idx = i

    sequence = get_sequence(array, sequences, max_idx)
    return [sums[max_idx], sequence]


if __name__ == '__main__':
    array = [10, 70, 20, 30, 50, 11, 30]
    res = max_sum_inc_sub(array)
    print(f'res {res}')

    array = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]
    res = max_sum_inc_sub(array)
    print(f'res {res}')
