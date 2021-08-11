import string

# n - length of the string
# c - num chars a-z = 26
# O(n) time
# O(1) space (always 26 elements in length)

def first_non_repeating_char(text: str):
    """Finds index of first non repeating char"""
	char_counts = [0] * len(string.ascii_lowercase)
	
	for char in text:
		idx = ord(char) - ord('a')
		char_counts[idx] += 1
		
	for idx, char in enumerate(text):
		count_idx = ord(char) - ord('a')
		if char_counts[count_idx] == 1:
			return idx
		
    return -1
