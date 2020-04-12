from collections import Counter
import heapq


def top_k_frequent(nums, k):
    counter = Counter(nums)
    heap = []

    for (num, count) in counter.items():
        if len(heap) == k:
            heapq.heappushpop(heap, (count, num))
        else:
            heapq.heappush(heap, (count, num))

    return [num for (count, num) in heap]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent(nums, k)
    print(f'result -> {result}')
