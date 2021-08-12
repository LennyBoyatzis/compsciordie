# n number of students in a row (half the class)
# O(n log n) - Sorting time complexity
# O(1) - Sorting can be done in place to reduce space requirements

# Cause we are talking about heights (are there constraints - i.e. max heights)
# If there were constaints i.e. heights never passed 10
# We can make the sorting process more efficient
# [0] * len(max_height)
# We can store counts of the heights as we see them
# Could do this for both lists of heights, then loop through and compare the counts

def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	back_row = redShirtHeights if redShirtHeights[0] >= blueShirtHeights[0] else blueShirtHeights
	front_row = redShirtHeights if redShirtHeights[0] < blueShirtHeights[0] else blueShirtHeights
	
	for i in range(len(back_row)):
		back_height, front_height = back_row[i], front_row[i]
		if back_height <= front_height:
			return False
	return True	
