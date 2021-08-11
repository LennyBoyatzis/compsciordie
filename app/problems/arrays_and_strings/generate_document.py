from collections import Counter

# n - length of characters
# m - length of document
# c - num unique chars in the characters string
# O(n + m) time
# O(c) space

def generate_document(characters: str, document: str) -> bool:
	"""Determines whether a document can be generated from chars"""
	char_counts = Counter(characters)
	
	for char in document:
		if char in char_counts and char_counts[char] > 0:
			char_counts[char] -= 1
		else:
			return False
	return True
