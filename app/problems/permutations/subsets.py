def calc_subsets(nums):
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = calc_subsets(nums)
    print(f'result -> {result}')
