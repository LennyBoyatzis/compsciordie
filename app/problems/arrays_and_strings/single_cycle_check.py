def get_next_idx(current_idx, array):
    jump = array[current_idx]
    next_idx = (current_idx + jump) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)


def has_single_cycle(array):
    num_visited = 0
    current_idx = 0 
    while num_visited < len(array):
        if num_visited > 0 and current_idx == 0:
            return False
        num_visited += 1
        current_idx = get_next_idx(current_idx, array)
    return current_idx == 0 


if __name__ == '__main__':
    array = [2, 3, 1, -4, -4, 2]
    result = has_single_cycle(array)
    print(f'result {result}')

    # forwards = [2, 3, 5, -4, -4, 2]
    # next_idx = get_next_idx(2, forwards)
    # print(f'next_idx {next_idx}') # 1

    # backwards = [2, 3, 0, -4, -4, 2]
    # next_idx = get_next_idx(2, backwards)
    # print(f'next_idx {next_idx}') # 3
