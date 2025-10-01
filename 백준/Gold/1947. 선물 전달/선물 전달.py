import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    dp = [0] * (n + 3)
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        dp[i] = ((dp[i - 1] + dp[i - 2]) * (i - 1)) % 1_000_000_000
    print(dp[n])


main()
