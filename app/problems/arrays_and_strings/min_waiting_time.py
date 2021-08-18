# n = number of queries
# O(n log n) runtime (sorting)
# O(1) space (sort in place)

def minimum_waiting_time(queries: List[int]) -> int:
    """Returns min waiting time for queries"""
	min_waiting_time = 0
	cumsum = 0
	queries.sort()
	
	for i in range(1, len(queries)):
		cumsum += queries[i-1]
		min_waiting_time += cumsum
		
	return min_waiting_time
