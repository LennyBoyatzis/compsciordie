def move_zeros_to_end(nums):
    swap_index, size = 0, len(nums)

    for i in range(size):
        if nums[i] != 0:
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index += 1

    return nums


if __name__ == '__main__':
    nums = [1, 0, 1, 0, 0, 0, 1, 1, 0]
    result = move_zeros_to_end(nums)
    print(f'result -> {result}')
