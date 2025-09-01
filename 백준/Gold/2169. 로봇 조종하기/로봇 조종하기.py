import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


MIN = float("-inf")


def solution(left_prefix, right_prefix, arr, visited, pos):
    x, y = pos


def main():
    global n, m

    n, m = map(int, input().split())
    arr = [[0] * (m + 2)]
    for _ in range(n):
        arr.append([0] + list(map(int, input().split())) + [0])

    dp = [[MIN] * (m + 1) + [MIN] for _ in range(n + 1)]
    dp[1][0] = dp[0][1] = 0
    for i in range(1, m + 1):
        dp[1][i] = dp[1][i - 1] + arr[1][i]

    for i in range(2, n + 1):
        right_prefix = [MIN] * (m + 2)
        left_prefix = [MIN] * (m + 2)
        for j in range(1, m + 1):
            left_prefix[j] = max(dp[i - 1][j], left_prefix[j - 1]) + arr[i][j]
            right_prefix[m - j + 1] = (
                max(dp[i - 1][m - j + 1], right_prefix[m - j + 1 + 1])
                + arr[i][m - j + 1]
            )
        for j in range(1, m + 1):
            dp[i][j] = max(left_prefix[j], right_prefix[j])

    print(dp[n][m])


main()
