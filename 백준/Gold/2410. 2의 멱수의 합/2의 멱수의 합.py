import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    dp = [0] * (n + 1)
    dp[0] = 1

    i = 1
    while i <= n:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
        i *= 2
    print(dp[n] % 1_000_000_000)


main()
