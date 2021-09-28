# Bottom Up DP Approach

# O(n) runtime
# O(1) space

def tribonacci(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1

    ans = [0, 1, 1]

    for i in range(3, n+1):
        t_n = sum(ans)
        ans[0] = ans[1]
        ans[1] = ans[2]
        ans[3] = t_n

    return ans[-1]

if __name__ == '__main__':
    res = tribonacci(5)
    print(f'res {res}')
