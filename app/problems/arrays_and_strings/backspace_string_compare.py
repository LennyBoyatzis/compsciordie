def backspace_string_compare(S, T):
    def build(S):
        stack = []
        for c in S:
            if c is not '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)
    return build(S) == build(T)


if __name__ == '__main__':
    S = 'dafsdfs###c'
    T = 'dafsd#c'
    result = backspace_string_compare(S, T)
    print(result)
