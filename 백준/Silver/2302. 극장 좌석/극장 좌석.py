import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())  # 최대 1 <= n <= 40
    m = int(input())
    fixed_seats = set(int(input()) for _ in range(m))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    if 1 < n and 1 not in fixed_seats:
        dp[1][2] = 1

    for i in range(2, n + 1):
        dp[i][i] = dp[i - 1][i - 1] + dp[i - 1][i - 2]
        if i in fixed_seats:
            continue

        dp[i][i - 1] = dp[i - 1][i]
        if i < n:
            dp[i][i + 1] = dp[i - 1][i - 1] + dp[i - 1][i - 2]

    # for row in dp:
    #     print(row)
    print(sum(dp[n]))

    # dp[i] = i번까지 배치할 경우 경우의 수?

    # 1 2 3 -> 1 3 2
    #
    # 1 2 4 3
    # 2번자리에 3번이 있다면 1번은 자동으로 1번 3번자리는 자동으로 2번
    # dp[3][2] 3번 자리에 2번을 둘 경우
    # dp[3][2] = dp[2][3]
    # dp[3][3] = dp[2][2] + dp[2][1]
    # dp[3][4] = dp[2][2] + dp[2][1]


main()
