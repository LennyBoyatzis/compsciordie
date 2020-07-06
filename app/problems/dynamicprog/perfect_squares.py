def num_squares(n: int) -> int:
    """Returns min number of perfect square that sum to n"""
    square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i-square] + 1)
    return dp[-1]


if __name__ == '__main__':
    n = 13
    result = result(n)
    print(f'result: {result}')
