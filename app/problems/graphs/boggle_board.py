def build_trie(words):
    trie = {}

    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = word
    return trie


def get_adjacent_cells(board, cell):
    n_rows, n_cols = len(board), len(board[0])
    r, c = cell
    directions = [(-1, 1), (-1, 0), (1, -1), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1)]
    in_bounds = []

    for r_off, c_off in directions:
        if 0 <= r + r_off < n_rows and 0 <= c + c_off < n_cols:
            in_bounds.append((r + r_off, c + c_off))
    return in_bounds


def search(board, cell, trie_node, visited, words):
    if cell in visited:
        return

    i, j = cell
    letter = board[i][j]

    if letter not in trie_node:
        return

    visited.add(cell)
    trie_node = trie_node[letter]

    if '*' in trie_node:
        words.append(trie_node['*'])

    neighbours = get_adjacent_cells(board, cell)

    for neighbour in neighbours:
        search(board, neighbour, trie_node, visited, words)

    visited.remove(cell) 


def boggle_board(board, words):
    n_rows, n_cols = len(board), len(board[0])
    trie = build_trie(words)
    ans = []

    for i in range(n_rows):
        for j in range(n_cols):
            cell = (i, j)
            letter = board[i][j]
            search(board, cell, trie, set(), ans)
    return list(set(ans))


if __name__ == '__main__':
    board = [
        ['t', 'h', 'i', 's', 'i', 's', 'a'],
        ['s', 'i', 'm', 'p', 'l', 'e', 'x'],
        ['b', 'x', 'x', 'x', 'x', 'e', 'b'],
        ['x', 'o', 'g', 'g', 'l', 'x', 'o'],
        ['x', 'x', 'x', 'D', 'T', 'r', 'a'],
        ['R', 'E', 'P', 'E', 'A', 'd', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['N', 'O', 'T', 'R', 'E', '-', 'P'],
        ['x', 'x', 'D', 'E', 'T', 'A', 'E']]

    words = ['this', 'is', 'not', 'a', 'simple', 'boggle', 'board', 'test', 'REPEATED', 'NOTRE-PEATED']
    res = boggle_board(board, words)
    print(f'res {res}')

