# How can we calculate the height at any given index i?
# Depends on the min(highest_tower_to_left, highest_tower_to_right) - pillar height
# Can we build up arrays storing the highest tower left and highest tower right
# at each index

def water_area(heights):
    size = len(heights)
    ans = [0 for _ in range(size)]
    left_max = 0

    for i in range(size):
        height = heights[i]
        ans[i] = left_max
        left_max = max(left_max, height)

    right_max = 0

    for i in range(size-1, -1, -1):
        height = heights[i]
        min_height = min(ans[i], right_max)
        ans[i] = max(min_height - height, 0)
        right_max = max(right_max, height)

    return sum(ans)


if __name__ == '__main__':
    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    ans = water_area(heights)
    print(f'ans {ans}')
