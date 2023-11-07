def sol():
    n = int(input())
    dp = [n for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 3:
            dp[i] = 1
        elif i == 5:
            dp[i] = 1
        elif 5 < i:
            if dp[i - 3] != n:
                dp[i] = dp[i - 3] + 1
            if dp[i - 5] != n:
                dp[i] = min(dp[i], dp[i - 5] + 1)
    if dp[-1] == n:
        print(-1)
    else:
        print(dp[-1])


sol()
