def balanced_parens(parens, current_idx = 0, paren_diff = 0):
    """Returns bool if array contains balanced parens"""
    if current_idx == len(parens):
        return paren_diff == 0

    if paren_diff < 0:
        return False

    if parens[current_idx] == '(':
        return balanced_parens(parens, current_idx + 1, paren_diff + 1)
    elif parens[current_idx] == ')':
        return balanced_parens(parens, current_idx + 1, paren_diff - 1)


if __name__ == '__main__':
    res = balanced_parens(['(', ')', '(', ')'])
    expected = True 
    print(f'res {res}')
    assert res == expected 
