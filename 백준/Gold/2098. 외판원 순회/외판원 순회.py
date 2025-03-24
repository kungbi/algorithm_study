import sys
import operator

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def solution(W, dp, node, visited):
    if visited == (1 << n) - 1:
        if W[node][0] == 0:
            return float("inf")
        return W[node][0]
    if dp[visited][node] != -1:
        return dp[visited][node]

    min_cost = float("inf")
    for n_node in range(n):
        if W[node][n_node] == 0:
            continue
        if visited & (1 << n_node):
            continue

        cost = solution(W, dp, n_node, visited | (1 << n_node)) + W[node][n_node]
        min_cost = min(cost, min_cost)

    dp[visited][node] = min_cost
    return min_cost


n = None


def main():
    global n

    n = int(input())
    W = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * n for _ in range(2**n)]
    solution(W, dp, 0, 1)
    print(dp[1][0])


main()
