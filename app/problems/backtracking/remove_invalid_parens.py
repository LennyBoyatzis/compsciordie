def is_valid(s):
    stack = []

    for char in s:
        if char is '(':
            stack.append(char)
        elif char is ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

"""
Time Limit Exceeded
"""

def remove_invalid_parens(s):
    ans = set()
    min_removed = float('inf')

    def backtrack(substring):
        nonlocal ans
        nonlocal min_removed

        if is_valid(substring):
            rem_count = len(s) - len(substring)

            if rem_count <= min_removed:

                if rem_count < min_removed:
                    ans = set()
                    min_removed = rem_count

                ans.add(substring)
        else:
            for index, char in enumerate(substring):
                if char is '(' or char is ')':
                    backtrack(substring[:index] + substring[index+1:])

    backtrack(s)
    return list(ans)


if __name__ == '__main__':
    s = '()())()'
    assert remove_invalid_parens(s) == ["()()()", "(())()"]

    s2 = '(a)())()'
    assert remove_invalid_parens(s2) == ["(a)()()", "(a())()"]

    s3 = ')('
    assert remove_invalid_parens(s3) == [""]
