import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    dp = [0] * (n + 1 + 4)
    dp[0] = 1

    dp[2] = 3
    dp[4] = 3 * 3 + 2

    for i in range(5, n + 1):
        dp[i] = dp[i - 2] * 3 + dp[i - 4] * 2
        if i % 2 == 0:
            for j in range(6, i + 1, 2):
                dp[i] += dp[i - j] * 2

    print(dp[n])


main()
