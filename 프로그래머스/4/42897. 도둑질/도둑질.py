def f(money, dp, n):
    for i in range(3, n):
        a = dp[i-3]
        b = dp[i-2]
        
        if a > b:
            dp[i] = a + money[i]
        else:
            dp[i] = b + money[i]

def solution(money):
    n = len(money)
    dp1 = [0] * (n - 1)
    dp2 = [0] * (n - 1)
    
    dp1[0] = money[0]
    dp1[1] = money[1]
    dp1[2] = dp1[0] + money[2]
    f(money, dp1, n - 1)
    
    
    dp2[0] = money[1]
    dp2[1] = money[2]
    dp2[2] = dp2[0] + money[3]
    f(money[1:], dp2, n - 1)
    return max(max(dp1), max(dp2))