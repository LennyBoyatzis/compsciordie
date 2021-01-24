from collections import defaultdict


def subarray_sum_equals_k(s, k):
    """
    Given an array of integers, nums and an integer k, return the total number
    of continuous subarrays whose sum equals to k
    """
    ans = 0

    for i in range(len(s)):
        subarray_sum = s[i] 

        for j in range(i+1, len(s)):
            subarray_sum += s[j] 

            if subarray_sum == k:
                ans += 1

    return ans


if __name__ == '__main__':
    nums = [1, -9, 12, 4, 10]
    k = 3
    result = subarray_sum_equals_k(nums, k)
    print(f'result -> {result}')
