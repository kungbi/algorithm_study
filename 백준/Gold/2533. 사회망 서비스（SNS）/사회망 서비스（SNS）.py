import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def solution(edges, dp, visited, node):
    visited[node] = True

    dp[node][1] = 1
    for n_node in edges[node]:
        if visited[n_node]:
            continue

        solution(edges, dp, visited, n_node)
        dp[node][0] += dp[n_node][1]
        dp[node][1] += min(dp[n_node][1], dp[n_node][0])


def main():
    n = int(input())

    dp = [[0] * 2 for _ in range(n + 1)]
    edges = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    visited = [False] * (n + 1)
    solution(edges, dp, visited, 1)

    print(min(dp[1]))


main()
