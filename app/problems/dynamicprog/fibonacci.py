

#        5
#     /     \  
#    4        3
#   / \      /  \ 
#  3    2    2   1
# / \  / \
# 2  1 1  0

# f(0) = 0
# f(1) = 1
# f(2) = 0 + 1 = 1
# f(3) = 1 + 1 = 2

# Raw Recursion
# O(b^d)
# O(2^n) runtime
# O(n) space

# Recursion with memoization
# O(b*d)
# O(2*n) runtime
# O(b*d) space (???)


def recurse(n, cache):
    if n in cache:
        return cache[n]

    if n < 2:
        return n

    results = recurse(n-2, cache) + recurse(n-1, cache)
    cache[n] = results
    return results


def fib(n):
    cache = {}
    return recurse(n, cache)

if __name__ == '__main__':
    res = fib(5)
    print(f'res {res}')
