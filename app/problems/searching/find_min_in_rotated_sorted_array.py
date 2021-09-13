def find_min_in_rotated_array(nums):
    left, right = 0, len(nums) - 1

    if len(nums) == 1:
        return nums[0]

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1

    return nums[right+1] if right != len(nums) - 1 else nums[0]


if __name__ == '__main__':
    # nums = [4, 5, 6, 7, 0, 1, 2]
    nums = [3, 1, 2]
    res = find_min_in_rotated_array(nums)
    print(f'res {res}')
