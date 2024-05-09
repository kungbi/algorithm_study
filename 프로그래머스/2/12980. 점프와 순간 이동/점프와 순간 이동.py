

def solution(n):
    dp = [0, 1, 1, 2, 1, 2, 2]
    
    answer = 0
    
    while len(dp) <= n:
        if n % 2 == 1:
            answer += 1
        n = n // 2

    return answer + dp[n]
