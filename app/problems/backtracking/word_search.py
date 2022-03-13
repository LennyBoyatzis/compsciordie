"""
Runtime Complexity
- O(N x 3**L)
- N is the number of cells on the board
- L is the length of the word

3**L
- 3-ary tree for backtracking function (3 possible directions to explore)
- Worst case is L levels in the recursive tree
- O(b**d), where b is branching factor, d is depth of the tree

Space Complexity
- O(L)
- Height of the recursive call stack
"""
def backtrack(board, row, col, suffix):
    ROWS = len(board)
    COLS = len(board[0])

    if len(suffix) == 0:
        return True

    if row < 0 or row == ROWS or col < 0 or col == COLS \
       or board[row][col] != suffix[0]:
        return False

    board[row][col] = '#'
    contains_word = False

    for row_offset, col_offset in [(1,0), (-1,0), (0,1), (0,-1)]:
        contains_word = backtrack(board, row+row_offset, col+col_offset, suffix[1:])
        if contains_word: break

    board[row][col] = suffix[0]
    return contains_word


def word_search(board, word):
    ROWS = len(board)
    COLS = len(board[0])

    for row in range(ROWS):
        for col in range(COLS):
            if backtrack(board, row, col, word):
                return True

    return False


if __name__ == '__main__':
    board = [
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","B"],
        ["A","A","A","A","B","A"]
    ]

    word = "AAAAAAAAAAAAABB"
    ans = word_search(board, word)
    assert ans == False

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]

    word = "ABCCED"
    ans = word_search(board, word)
    assert ans == True

    word = "SEE"
    ans = word_search(board, word)
    assert ans == True

    word = "ABCB"
    ans = word_search(board, word)
    assert ans == False

    board = [
        ["a"]
    ]

    word = "a"
    ans = word_search(board, word)
    assert ans == True
