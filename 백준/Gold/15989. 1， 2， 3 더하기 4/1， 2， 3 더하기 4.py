import sys


def input():
    return sys.stdin.readline().rstrip()


MAX = 10_000


def main():
    dp = [1] * (MAX + 1)
    dp[2] = 2
    for i in range(3, MAX + 1):
        dp[i] += dp[i - 2]

    for i in range(3, MAX + 1):
        dp[i] += dp[i - 3]

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp[n])


main()
