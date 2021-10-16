def get_max_value(n, stacks):
    max_val = 0
    stack_sizes = [len(stack) for stack in stacks]
    stack_heads = [0 for _ in range(len(stacks))]

    # Note arrays in python are passed by reference
    # Pass a copy of the array to ensure each recursive call has its unique
    # stack_heads array
    def search(n, path_sum, stack_heads):
        nonlocal max_val

        if n == 0:
            max_val = max(max_val, path_sum)
            return

        for i in range(len(stacks)):
            has_capacity = stack_heads[i] < stack_sizes[i]
            if has_capacity:
                print(stack_heads)
                value = stacks[i][stack_heads[i]]
                stack_heads[i] += 1
                search(n-1, path_sum + value, stack_heads[:])

    search(n, 0, stack_heads)
    return max_val


if __name__ == '__main__':
    stacks = [
        [10, 4, 1],
        [2, 2, 40]]

    res = get_max_value(3, stacks)
    assert res == 44

    res = get_max_value(4, stacks)
    assert res == 54

    res = get_max_value(5, stacks)
    assert res == 58

    res = get_max_value(6, stacks)
    assert res == 59

    stacks = [
        [1, 1, 100, 3],
        [2000, 2, 3, 1],
        [10, 1, 4]]

    res = get_max_value(2, stacks)
    print(f'res {res}')
    assert res == 2010

    res = get_max_value(3, stacks)
    print(f'res {res}')
    assert res == 2012

    # res = get_max_value(4, stacks)
    # print(f'res {res}')
    # assert res == 2102
