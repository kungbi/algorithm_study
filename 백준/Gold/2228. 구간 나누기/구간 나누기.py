import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(idx, section):
    global visited

    if section == 0:
        return 0
    if idx < 0:
        return float("-inf")

    if visited[idx][section] == True:
        return dp[idx][section]

    visited[idx][section] = True
    dp[idx][section] = solution(idx - 1, section)  # 포함하지 않을 경우
    for i in range(idx, 0, -1):  # 포함
        dp[idx][section] = max(
            dp[idx][section],
            solution(i - 2, section - 1) + prefix_sum[idx] - prefix_sum[i - 1],
        )
    return dp[idx][section]


def main():
    global dp, prefix_sum, visited

    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    dp = [[float("-inf")] * (n + 1) for _ in range(n + 1)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    print(solution(n, m))


main()
