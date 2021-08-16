from typing import List

# n = number of coins
# O(n log n) runtime (sorting)
# O(1) space

def non_constructible_change(coins: List[int]) -> int:
    """Returns min amount of change not able to be created"""
	if not coins:
		return 1
	
	coins.sort()
	current_change = 0 
	
	for coin in coins:
		if coin > current_change + 1:
			return current_change + 1
		current_change += coin
		
	return current_change + 1
