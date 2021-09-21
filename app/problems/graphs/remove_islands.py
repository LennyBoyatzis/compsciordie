from collections import deque


def get_adjacent_cells(cell, matrix):
	n_rows, n_cols = len(matrix), len(matrix[0])
	offsets = [(1,0), (-1,0), (0,1), (0,-1)]
	neighbours = []
	r, c = cell

	for r_off, c_off in offsets:
		if (0 <= r+r_off < n_rows) and (0 <= c+c_off < n_cols):
			if matrix[r+r_off][c+c_off] == 1:
				neighbours.append((r+r_off, c+c_off))

	return neighbours


def traverse(start, matrix):
    queue = deque([start])

    while queue:
	    node = queue.pop()
	    r, c = node
	    node_val = matrix[r][c]
	    matrix[r][c] = -1 # mark as connected to edge
	    neighbours = get_adjacent_cells(node, matrix)

	    for neighbour in neighbours:
	        queue.appendleft(neighbour)


def remove_islands(matrix):
	n_rows, n_cols = len(matrix), len(matrix[0])

	# Iterate first row
	for j in range(n_cols):
		first_row = 0
		val = matrix[first_row][j]
		if val == 1:
		    print(f'found edge start {first_row}, {j}')
		    traverse((first_row, j), matrix)
			
	# Iterate last row
	for j in range(n_cols):
		last_row = n_rows - 1
		val = matrix[last_row][j]
		if val == 1:
		    print(f'found edge start {last_row}, {j}')
		    traverse((last_row, j), matrix)

	# Iterate first col
	for i in range(n_rows):
		first_col = 0
		val = matrix[i][first_col]
		if val == 1:
		    print(f'found edge start {i}, {first_col}')
		    traverse((i, first_col), matrix)

	# Iterate last col
	for i in range(n_rows):
		last_col = n_cols - 1 
		val = matrix[i][last_col]
		if val == 1:
		    print(f'found edge start {i}, {last_col}')
		    traverse((i, last_col), matrix)

	# Modify the matrix
	for i in range(n_rows):
		for j in range(n_cols):
			val = matrix[i][j]

			if val == -1:
				matrix[i][j] = 1
			elif val == 1:
				matrix[i][j] = 0

	return matrix


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]]

    res = remove_islands(matrix)
    print(f'res {res}')

    # cells = get_adjacent_cells((1, 5), matrix)
    # print(f'cells {cells}')

    # cells = get_adjacent_cells((1, 4), matrix)
    # print(f'cells {cells}')
