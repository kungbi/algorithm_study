import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())

    # n = 10
    # 0 + 10, 10을 k-1 개로 나눈 것들
    # 1 + 9, 9를 k-1 개로 나눈 것들
    # dp[i][j] = i를 만들기 위해 k개의 정수를 사용할때의 경우의 수.

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][1] = 1

    for nn in range(n + 1):
        for kk in range(2, k + 1):
            for i in range(nn + 1):
                dp[nn][kk] += dp[nn - i][kk - 1]
                dp[nn][kk] %= 1_000_000_000
    # for idx, row in enumerate(dp):
    #     print(idx, row)
    print(dp[n][k] % 1_000_000_000)


main()
