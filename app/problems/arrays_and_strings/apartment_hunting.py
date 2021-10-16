def apartment_hunting(blocks, reqs):
    num_amenities = len(reqs)
    num_blocks = len(blocks)
    dp = [[float('inf') for _ in range(num_amenities)] for _ in
          range(num_blocks)]

    prev_closest_indices = [None] * num_amenities

    for i in range(num_blocks):
        for j, req in enumerate(reqs):
            contains_amenity = blocks[i][req]
            if contains_amenity:
                dp[i][j] = 0
                prev_closest_indices[j] = i
            else:
                if prev_closest_indices[j] is not None:
                    dp[i][j] = i - prev_closest_indices[j]

    prev_closest_indices = [None] * num_amenities

    for i in range(num_blocks):
        end = num_blocks - 1
        for j, req in enumerate(reqs):
            contains_amenity = blocks[end-i][req]
            if contains_amenity:
                dp[end-i][j] = 0
                prev_closest_indices[j] = i
            else:
                if prev_closest_indices[j] is not None:
                    dp[end-i][j] = min(dp[end-i][j], i - prev_closest_indices[j])

    max_dists = [max(dists) for dists in dp]
    min_dist = min(max_dists)
    min_idx = max_dists.index(min_dist)
    return min_idx

if __name__ == '__main__':
    blocks = [
        {
            'gym': False,
            'school': True,
            'store': False
        },
        {
            'gym': True,
            'school': False,
            'store': False
        },
        {
            'gym': True,
            'school': True,
            'store': False
        },
        {
            'gym': False,
            'school': True,
            'store': False
        },
        {
            'gym': False,
            'school': True,
            'store': True
        }
    ]

    requirements = ['gym', 'school', 'store']

    res = apartment_hunting(blocks, requirements)
    print(f'res -> {res}')
