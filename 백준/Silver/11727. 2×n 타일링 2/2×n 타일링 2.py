import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    dp = [0] * (n + 4)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] * 2 + dp[i - 1]
    print(dp[n] % 10_007)


main()
