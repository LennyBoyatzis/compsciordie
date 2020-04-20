def permute(nums):
    if len(nums) == 1:
        return [nums]
    else:
        perms = []
        for i in range(len(nums)):
            digit = nums[i]
            remainder = nums[:i] + nums[i+1:]
            for perm in permute(remainder):
                perms.append([digit] + perm)
        return perms


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = permute(nums)
    # print(f'what is the result {result}')
