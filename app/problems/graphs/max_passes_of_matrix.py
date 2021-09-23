from collections import deque


def get_adjacent_neighbours(cell, matrix):
    r, c, _ = cell
    n_rows, n_cols = len(matrix), len(matrix[0])
    offsets = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbours = []

    for r_off, c_off in offsets:
        i, j = r + r_off, c + c_off
        in_bounds = (0 < i <= n_rows and 0 < j <= n_cols)
        if in_bounds:
            if matrix[i][j] < 0:
                neighbours.append((i, j))
    return neighbours


def search(nodes, matrix, neg_count):
	steps = 0
	queue = deque(nodes)
	neg_visited = 0

	while queue:
	    node = queue.pop()
	    r, c, count = node
	    steps = max(count, steps)

	    if neg_visited == neg_count:
	        return steps

        if matrix[r][c] < 0:
	        neg_visited += 1
	        matrix[r][c] *= -1

	    if matrix[r][c] > 0:
	        neighbours = get_adjacent_neighbours(node, matrix)
	        print(f'neighbours {neighbours}')
	        for neighbour in neighbours:
	            queue.appendleft((*neighbour, count+1))

	return -1

	
def min_passes_of_matrix(matrix):
	n_rows, n_cols = len(matrix), len(matrix[0])
	start_nodes = [] # [2]
	neg_count = 0 # 5
	
	for i in range(n_rows):
		for j in range(n_cols):
			val = matrix[i][j]
			if val > 0:
				start_nodes.append((i,j,0))
			if val < 0:
				neg_count += 1
	
	steps = search(start_nodes, matrix, neg_count)
	return steps


if __name__ == '__main__':
    matrix = [
        [0, -2, -1],
        [-5, 2,  0],
        [-6, -2, 0]]

    res = min_passes_of_matrix(matrix)
    print(f'res {res}')

