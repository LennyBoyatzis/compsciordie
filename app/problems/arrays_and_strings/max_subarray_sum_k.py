def max_subarray_len(nums, k):
    dic = {0: -1}
    total = 0
    maxlen = 0

    for i in range(len(nums)):
        total += nums[i]

        if total - k in dic and i-dic[total-k] > maxlen:
            maxlen = i-dic[total-k]
        if total not in dic:
            dic[total] = i
    return maxlen


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3
    result = max_subarray_len(nums, k)
    print(f'result: {result}')
