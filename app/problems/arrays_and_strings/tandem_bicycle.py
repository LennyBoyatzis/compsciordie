# n - number of tandem bicycles
# O(n log n) - sorting
# O(1) - sort in place

def tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest):
    """Returns min or max total speeds for tandem bicycles"""
	red_shirt_speeds.sort()
	blue_shirt_speeds.sort(reverse=fastest)
	ans = 0
	
	for i in range(len(red_shirt_speeds)):
		ans += max(red_shirt_speeds[i], blue_shirt_speeds[i])
	return ans
