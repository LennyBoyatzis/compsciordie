def permute(nums):
    n = len(nums)
    output = []

    def backtrack(first=0):
        if first == n:
            output.append(nums[:])

        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack()
    return output


def permute_2(nums):
    permutations = []

    if len(nums) == 1:
        permutations.append(nums)
    else:
        for index, num in enumerate(nums):
            rest = nums[:index] + nums[index+1:]
            for perm in permute(rest):
                permutations.append([num] + perm)
    return permutations


if __name__ == '__main__':
    digits = [1, 2, 3]
    results = permute(digits)
    print(f'results {results}')
    # [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
