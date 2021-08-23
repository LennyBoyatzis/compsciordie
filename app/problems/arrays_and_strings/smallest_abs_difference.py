from typing import List


def smallest_difference(arr_1: List[int], arr_2: List[int]) -> List[int]:
	"""Finds smallest abs difference between pairs from 2 arrays"""
	arr_1.sort()
	arr_2.sort()
	
	smallest_diff = float('inf')
	prev_diff = float('inf')
	smallest_pair = []
	
	p1_idx, p2_idx = 0, 0
	
	while p1_idx < len(arr_1) and p2_idx < len(arr_2):
		p1, p2 = arr_1[p1_idx], arr_2[p2_idx]
		
		if p1 < p2:
			diff = p2 - p1
			p1_idx += 1
		elif p2 < p1:
			diff = p1 - p2
			p2_idx += 1
		else:
			return [p1, p2]
	
		if diff < smallest_diff:
			smallest_diff = diff
			smallest_pair = [p1, p2]
	
	return smallest_pair
