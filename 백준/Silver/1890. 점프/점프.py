import sys


def input():
    return sys.stdin.readline().rstrip()


def is_frame(x, y, n):
    return 0 <= x < n and 0 <= y < n


def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for y in range(n):
        for x in range(n):
            if arr[y][x] == 0:
                continue
            nx = x + arr[y][x]
            ny = y + arr[y][x]

            if is_frame(x, ny, n):
                dp[ny][x] += dp[y][x]
            if is_frame(nx, y, n):
                dp[y][nx] += dp[y][x]
    print(dp[n - 1][n - 1])


main()
