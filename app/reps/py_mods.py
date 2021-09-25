import bisect
import heapq
from collections import Counter, deque


# bisect.bisect(array, target)
# return index where target would be inserted
# defaults to  bisect.bisect_left -> only relevant when duplicates are in array
# bisect.bisect_left(array, target)
# bisect.bisect_right(array, target)

# Note: be weary that the above isn't looking for exact matches
# It will return the end of a list if value is greater than last element
# It will return the start of a list if value is less than the first element

# bisect.insort(array, target)
# insertion sorts target into sorted array
# defaults to bisect.insort_left(array, target)

# heapq
# heapq.heapify(arr) # defaults to min heap
# heapq.heappush(arr, el)
# el = heapq.heappushpop(arr, el)
# heapq.heappop(arr)
# arr[0] get the min value in heap
heapq.nlargest(3, arr) # return 3 largest
heapq.nsmallest(3, arr) # return 3 smallest
