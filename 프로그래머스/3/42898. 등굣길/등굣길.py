
def solution(m, n, puddles):
    map = [[0] * (m + 1) for _ in range(n + 1)]
    for puddle in puddles:
        map[puddle[1]][puddle[0]] = 1
        
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if map[y][x] == 1:
                continue
            dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
    
    return dp[n][m] % 1000000007
    