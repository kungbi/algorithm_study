import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def solution(tree, node, dp, visited):
    visited[node] = True
    if dp[node] != -1:
        return dp[node]

    sum_num = 1
    for n_node in tree[node]:
        if visited[n_node] == True:
            continue
        sum_num += solution(tree, n_node, dp, visited)

    dp[node] = sum_num
    return dp[node]


def main():
    n, r, q = map(int, input().split())

    tree = dict()
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if not u in tree:
            tree[u] = []
        if not v in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)

    dp = [-1] * (n + 1)
    visited = [False] * (n + 1)
    solution(tree, r, dp, visited)
    for _ in range(q):
        node = int(input())
        print(dp[node])


main()
