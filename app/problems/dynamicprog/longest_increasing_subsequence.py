from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    """Returns longest increasing subsequence

    A subsequence of an nums is a set of numbers
    that aren't necessarily adjacent in the nums
    but are in the same order as they appear in
    the nums

    i.e. [1, 3, 4] is a subsequence of [1, 2, 3, 4]
    Space: O(n)
    Time: O(n^2)
    """
    size = len(nums)
    lengths = [1] * size
    sequences = [None] * size
    max_len_idx = 0

    for i in range(1, size):
        stop = nums[i]
        for j in range(i):
            if nums[j] < stop:
                if lengths[i] <= lengths[j] + 1:
                    lengths[i] = lengths[j] + 1
                    sequences[i] = j
        if lengths[i] >= lengths[max_len_idx]:
            max_len_idx = i

    ans = []
    curr_idx = max_len_idx

    while curr_idx is not None:
        ans.append(nums[curr_idx])
        curr_idx = sequences[curr_idx]

    return ans[::-1]


if __name__ == '__main__':
    nums = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
    result = longest_increasing_subsequence(nums)
    print(f'result {result}')
