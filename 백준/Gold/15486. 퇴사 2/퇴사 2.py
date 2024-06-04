import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    work_list = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)
    prev_max = 0

    for i in range(n):
        prev_max = max(prev_max, dp[i])

        end_idx = i + work_list[i][0]
        if end_idx <= n:
            dp[end_idx] = max(dp[end_idx], prev_max + work_list[i][1])

    print(max(dp))


solution()
