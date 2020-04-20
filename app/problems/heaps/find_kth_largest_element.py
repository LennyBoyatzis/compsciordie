import heapq


def find_kth_largest_element(nums, k):
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

    return heap[0]


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = find_kth_largest_element(nums, k)
    print(f'result -> {result}')
