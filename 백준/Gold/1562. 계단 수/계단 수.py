import sys


def solution(dp, x, y):
    for i in range(1024):
        if 0 <= x - 1 and dp[y - 1][x - 1][i]:
            set_id = (1 << x) | i
            dp[y][x][set_id] += dp[y - 1][x - 1][i]

        if x + 1 <= 9 and dp[y - 1][x + 1][i]:
            set_id = (1 << x) | i
            dp[y][x][set_id] += dp[y - 1][x + 1][i]


def main():
    n = int(input())
    dp = [[[0] * 1024 for _ in range(10)] for _ in range(n)]

    for y in range(n):
        for x in range(10):
            if y == 0:
                if x != 0:
                    dp[y][x][1 << x] += 1
                continue
            solution(dp, x, y)

    answer = 0
    for i in range(10):
        answer += dp[n - 1][i][1023]
    print(answer % 1_000_000_000)


main()
