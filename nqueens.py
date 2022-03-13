"""
Given a board of size n
- how many ways can you place n queens without, with all queens being in a
neutral position

Subproblems
- How to know if a square is neutral?
"""

def nqueens(n):
    def backtrack(row, cols, diags, anti_diags):
        # Have we reached end goal
        if row == n:
            return 1

        solutions = 0

        # Explore candidates
        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col

            if not (col in cols
                    or curr_diag in diags
                    or curr_anti_diag in anti_diags):

                # Place candidate
                cols.add(col)
                diags.add(curr_diag)
                anti_diags.add(curr_anti_diag)

                solutions += backtrack(row+1, cols, diags, anti_diags)

                # Retreat
                cols.remove(col)
                diags.remove(curr_diag)
                anti_diags.remove(curr_anti_diag)

        return solutions
    return backtrack(0, set(), set(), set())



if __name__ == '__main__':
    n = 4 
    ans = nqueens(n)
    print(f'ans {ans}')
