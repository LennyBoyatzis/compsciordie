import heapq

# dir(heapq)
# heapify
# heappop
# heappush
# heappushpop
# heapreplace
# merge
# nlargest
# nsmallest

# DEFAULT: Min Heap

def min_heap():
    arr = [20, -10, 44, 17, 8]
    heapq.heapify(arr) # [-10, 8, 44, 17, 20]
    print(arr)

    heapq.heappush(arr, -100) # [-100, 8, -10, 17, 20, 44] 
    print(arr)

    min_el = heapq.heappop(arr) # -100 
    print(min_el) # -100
    print(arr) # [-10, 8, 44, 17, 20]

    min_el = heapq.heappushpop(arr, 400)
    print(min_el) # -10
    print(arr) # [8, 17, 44, 400, 20]

    heapq.nlargest(3, arr) # [400, 44, 20]
    heapq.nsmallest(3, arr) # [8, 17, 20]

# _heapify_max
# _heappop_max
# _heapreplace_max

def max_heap():
    arr = [20, -10, 44, 17, 8]
    heapq._heapify_max(arr) # [44, 17, 20, -10, 8]
    print(arr)

    max_el = heapq._heappop_max(arr)
    print(max_el) # 44
    print(arr) # [20, 17, 8, -10]

    # _heapreplace_max is similar to heappushpop
    max_el = heapq._heapreplace_max(arr, 12)
    print(max_el) # 200 
    print(arr) # [17, 12, 8, -10]


class HeapNode:
    def __init__(self, value):
        self.value = value

    def __lt__(self, value):
        return self.value[1] < value

    def __gt__(self, value):
        return self.value[1] > value


def heap_with_complex_types():
    arr = [20, -10, 44, 17, 8]
    arr_heap_nodes = [HeapNode((idx, val)) for idx, val in enumerate(arr)]
    print(arr_heap_nodes)

    heapq.heapify(arr_heap_nodes)
    min_el = heapq.heappop(arr_heap_nodes)
    print(min_el.value)


if __name__ == '__main__':
    heap_with_complex_types()
