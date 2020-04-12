def generate_parenthesis(n):
    ans = []

    def backtrack(parens='', openers=0, closers=0):
        if len(parens) == n * 2:
            ans.append(parens)
            return

        if openers < n:
            backtrack(parens + '(', openers+1, closers)

        if closers < openers:
            backtrack(parens + ')', openers, closers+1)

    backtrack()
    return ans


if __name__ == '__main__':
    num = 3
    results = generate_parenthesis(num)
    print(f'results {results}')
