import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    c, n = map(int, input().split())
    cities = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [float("inf")] * (c + 101)
    dp[0] = 0

    for city in cities:
        cost, count = city
        for i in range(c + 1):
            dp[i + count] = min(dp[i + count], dp[i] + cost)
            i += count
    print(min(dp[c:]))


main()
