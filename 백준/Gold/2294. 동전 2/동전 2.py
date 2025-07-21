import sys


def input():
    return sys.stdin.readline().rstrip()


MAX = float("inf")


def main():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort()

    dp = [MAX] * (k + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    print(dp[k] if dp[k] != MAX else -1)


main()
