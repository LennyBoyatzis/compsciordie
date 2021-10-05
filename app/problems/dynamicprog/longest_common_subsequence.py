def longest_common(str1, str2):
    dp = [['' for _ in range(len(str1)+1)]
          for _ in range(len(str2)+1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str2[i-1] == str1[j-1]: 
                dp[i][j] = dp[i-1][j-1] + str2[i-1] 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)

    return dp[-1][-1]


if __name__ == '__main__':
    str1 = 'clement'
    str2 = 'antoine'
    result = longest_common(str1, str2) # ['X', 'Y', 'Z', 'W']
    print(f'result {result}')
