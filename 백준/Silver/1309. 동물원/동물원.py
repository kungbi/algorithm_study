import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = dp[0][1] = dp[0][2] = 1

    for i in range(1, n):
        dp[i][0] = sum(dp[i - 1]) % 9901
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901
    print(sum(dp[-1]) % 9901)


main()
