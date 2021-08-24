from typing import List

# n = length of array
# Average Case: O(n) time | O(n) space
# Worst Case: O(n) time | O(n) space

def max_subset_no_adjacent(array: List[int]) -> int:
	"""Finds max sum of non adjacent elements in array"""
	if not array:
		return 0
	elif len(array) == 1:
		return array[0]
	elif len(array) == 2:
		return max(array[0], array[1])
	else:
        dp = [0] * len(array)
            dp[0], dp[1] = array[0], max(array[0], array[1])

        for i in range(2, len(array)):
                dp[i] = max(dp[i-1], array[i] + dp[i-2])
        return dp[-1]
