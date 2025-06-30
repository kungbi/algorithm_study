import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = [0] + [int(input()) for _ in range(n)]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        curr = arr[i]
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]
        for j in range(curr):
            dp[i][curr] = max(dp[i][curr], dp[i - 1][j] + 1)

    # for row in dp:
    #     print(row)
    print(n - max(dp[n]))


main()
