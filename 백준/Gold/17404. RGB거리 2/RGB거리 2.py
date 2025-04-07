import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(start_color, rgb_cost, dp, n):
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb_cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb_cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb_cost[i][2]

    result = float("inf")
    for i in range(3):
        if i == start_color:
            continue
        result = min(result, dp[n - 1][i])
    return result


def main():
    n = int(input())
    rgb_cost = []
    for _ in range(n):
        rgb_cost.append(tuple(map(int, input().split())))

    answer = float("inf")
    for i in range(3):
        dp = [[float("inf")] * 3 for _ in range(n + 1)]
        for j in range(3):
            dp[0][j] = rgb_cost[0][j] if i == j else float("inf")
        answer = min(answer, solution(i, rgb_cost, dp, n))

    return answer


print(main())
