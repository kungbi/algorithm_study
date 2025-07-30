import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    secret = input()
    n = len(secret)
    if secret[0] == "0":
        return 0

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        if 10 <= int(secret[i - 2 : i]) <= 26:
            dp[i] += dp[i - 2]
            dp[i] %= 1_000_000
        if 0 < int(secret[i - 1]):
            dp[i] += dp[i - 1]
            dp[i] %= 1_000_000

    return dp[n]


print(main())
