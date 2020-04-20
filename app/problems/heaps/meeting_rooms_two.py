import heapq


def min_meeting_rooms(intervals):
    intervals.sort(key=lambda s: s[0])
    heap = []
    max_len = 0

    for (start, end) in intervals:
        if not heap:
            heapq.heappush(heap, end)
        elif start >= heap[0]:
            heapq.heappushpop(heap, end)
        else:
            heapq.heappush(heap, end)

        max_len = max(max_len, len(heap))

    return max_len


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    result = min_meeting_rooms(intervals)
    print(f'result -> {result}')
