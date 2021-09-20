from collections import deque


def get_adjacent_cells(cell, matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])
    offsets = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbours = []

    for r_off, c_off in offsets:
        r, c = cell
        if (0 <= r + r_off < n_rows) and (0 <= c + c_off < n_cols):
            neighbours.append((r+r_off, c+c_off))

    return neighbours


def breadth_first_search(start, matrix):
	queue = deque([start])
	visited = set()

	while queue:
		node = queue.pop()
		node_r, node_c = node
		node_val = matrix[node_r][node_c]
		visited.add(node)
		neighbours = get_adjacent_cells(node, matrix)
		
		for neighbour in neighbours:
			r, c = neighbour
			neighbour_val = matrix[r][c]
			if neighbour_val >= node_val:
				queue.appendleft(neighbour)

	return visited


def find_water_supply(matrix, v1, v2):
	v1_upstream = breadth_first_search(v1, matrix)
	v2_upstream = breadth_first_search(v2, matrix)

	inter_x = v1_upstream.intersection(v2_upstream)
	max_tower = float('-inf')
	max_cell = None

	for cell in inter_x:
		r, c = cell
		cell_val = matrix[r][c]
		if cell_val > max_tower:
			max_cell = cell

	return max_cell
	

if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 1],
        [1, 6, 7, 4],
        [1, 5, 1, 3],
        [1, 4, 1, 2]]

    v1 = (3, 1)
    v2 = (3, 3)
    res = find_water_supply(matrix, v1, v2)
    print(f'res {res}')
