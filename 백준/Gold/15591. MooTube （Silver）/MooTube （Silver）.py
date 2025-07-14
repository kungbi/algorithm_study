import sys
from collections import deque
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution(start, graph, costs, n):
    queue = deque([(start, float("inf"))])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        node, cost = queue.popleft()
        for n_node, n_cost in graph[node]:
            if visited[n_node]:
                continue

            costs[start][n_node] = min(cost, n_cost)
            queue.append((n_node, costs[start][n_node]))
            visited[n_node] = True


def main():
    n, Q = map(int, input().split())
    costs = [[0] * (n + 1) for _ in range(n + 1)]
    graph = defaultdict(list)
    for _ in range(n - 1):
        p, q, r = map(int, input().split())
        costs[p][q] = r
        costs[q][p] = r
        graph[q].append((p, r))
        graph[p].append((q, r))

    for start in range(1, n + 1):
        solution(start, graph, costs, n)

    for _ in range(Q):
        k, v = map(int, input().split())
        result = 0
        for cost in costs[v]:
            if k <= cost:
                result += 1
        print(result)

    # for row in costs:
    #     print(row)


main()
