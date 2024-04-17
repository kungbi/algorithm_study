import sys


def input():
    return sys.stdin.readline().rstrip()


def f(dp):
    dp[1][1] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1
    for i in range(4, 10_000 + 1):
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
        dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3]


def solution():
    dp = [[0] * 4 for _ in range(10_000 + 1)]
    f(dp)

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(sum(dp[n]))


solution()
