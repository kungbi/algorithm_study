def f(dp, num):
    result = 0
    for i in range(num):
        result += dp[i] * dp[num - i - 1]
    return (result)

def solution(n):
    dp = [0 for _ in range(n + 2)]
    dp[0] = dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = f(dp, i)
        
    return (dp[n])