import heapq
import bisect


# Idea 1: Maintain Sorted Array of Window Elements 
# Time: O(n^2) - insort is O(n)
# Space: O(n)
def longest_subarray_sorting(nums, limit):
    start, ordered = 0, []

    for end in range(len(nums)):
        bisect.insort(ordered, nums[end])
        if ordered[-1] - ordered[0] > limit:
            ordered.pop(bisect.bisect(ordered, nums[start]) - 1)
            start += 1

    return end - start + 1

# Idea 2: Maintain 2 Heaps (Min & Max)
# Time: O(nlogn)
# Space: O(n)
def longest_subarray_heaps(nums, limit):
    max_heap, min_heap = [], []
    max_len = 0
    i = 0 # start of window index

    for j, num in enumerate(nums):
        heapq.heappush(max_heap, [num, j])
        heapq.heappush(min_heap, [num, j])

        while -max_heap[0][0] - min_heap[0][0] > limit:
            i = min(max_heap[0][1], min_heap[0][1]) + 1
            while max_heap[0][1] < i:
                heapq.heappop(max_heap)

            while min_heap[0][1] < i:
                heapq.heappop(min_heap)
            max_len = max(max_len, j-i-1)
    return max_len


if __name__ == '__main__':
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    ans = longest_subarray(nums, limit) # 4 [2, 4, 7, 2]
    print(f'ans {ans}')
