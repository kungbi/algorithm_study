import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    if n == 1:
        print(arr[0])
        return

    dp = [[0] * 3 for _ in range(n)]
    dp[0][1] = arr[0]
    dp[1][0] = arr[0]
    dp[1][1] = arr[1]
    dp[1][2] = arr[0] + arr[1]
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = arr[i] + dp[i - 1][0]
        dp[i][2] = arr[i] + dp[i - 1][1]

    print(max(dp[n - 1]))


main()
