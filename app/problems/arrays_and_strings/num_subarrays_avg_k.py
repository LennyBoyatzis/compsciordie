def num_subarrays_avg_k(arr, k, threshold):
    prefix_sum = [0]

    for num in arr:
        prefix_sum.append(num + prefix_sum[-1])

    return sum(prefix_sum[i+k] - prefix_sum[i] >= k * threshold for i in range(len(arr) - k + 1))




if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    result = num_subarrays_avg_k(arr, k, threshold)
    print(f'result -> {result}')
