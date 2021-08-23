from typing import List


def get_next_available_pos(arr: List[int], move: int, last_pos: int) -> int:
	"""Finds index of next available position"""
	while last_pos > 0 and arr[last_pos] == move:
		last_pos -= 1
	return last_pos


def move_element_to_end(arr: List[int], move: int) -> List[int]:
    """Moves all elements with a specific value to end of array"""
	head_idx = 0
	tail_idx = get_next_available_pos(arr, move, len(arr) - 1)
	
	while head_idx < tail_idx:
		head = arr[head_idx]
		if head == move:
			arr[head_idx], arr[tail_idx] = arr[tail_idx], arr[head_idx]
		
		head_idx += 1
		tail_idx = get_next_available_pos(arr, move, tail_idx)
	
	return arr
