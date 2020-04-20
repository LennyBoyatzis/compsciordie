def remove_invalid_parens(s):
    ans = set()
    min_removed = float('inf')

    def backtrack(s, index, open_count, close_count, expr, rem_count):
        nonlocal ans
        nonlocal min_removed

        if index == len(s):
            if open_count == close_count:
                if rem_count <= min_removed:
                    valid = "".join(expr)

                    if rem_count < min_removed:
                        ans = set()
                        min_removed = rem_count

                    ans.add(valid)
        else:
            current_char = s[index]
            if current_char not in ['(', ')']:
                expr.append(current_char)
                backtrack(s, index + 1, open_count, close_count, expr, rem_count)
                expr.pop()
            else:
                backtrack(s, index + 1, open_count, close_count, expr, rem_count + 1)
                expr.append(current_char)

                if s[index] == '(':
                    backtrack(s, index + 1, open_count + 1, close_count, expr, rem_count)
                elif close_count < open_count:
                    backtrack(s, index + 1, open_count, close_count + 1, expr, rem_count)

                expr.pop()
    backtrack(s, 0, 0, 0, [], 0)
    return list(ans)


if __name__ == '__main__':
    s = '()())()'
    # assert remove_invalid_parens(s) == ["()()()", "(())()"]
    result = remove_invalid_parens(s)
    print(f'result {result}')

    # s2 = '(a)())()'
    # assert remove_invalid_parens(s2) == ["(a)()()", "(a())()"]

    # s3 = ')('
    # assert remove_invalid_parens(s3) == [""]
