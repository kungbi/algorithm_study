import sys
from collections import defaultdict
from heapq import heappop
from heapq import heappush
from heapq import heapify


def input():
    return sys.stdin.readline().rstrip()


def dijkstra(n, edges, start):
    visited = [False] * (n + 1)
    costs = [float("inf")] * (n + 1)

    visited[start] = True
    costs[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heappop(heap)

        for n_node, n_cost in edges[node]:
            if visited[n_node]:
                continue
            if cost + n_cost < costs[n_node]:
                costs[n_node] = cost + n_cost
                heappush(heap, (costs[n_node], n_node))
    return costs


def main():
    n, e = map(int, input().split())
    edges = defaultdict(list)

    for _ in range(e):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))
    v1, v2 = map(int, input().split())

    start_costs = dijkstra(n, edges, 1)
    v1_costs = dijkstra(n, edges, v1)
    v2_costs = dijkstra(n, edges, v2)

    v1_first = start_costs[v1] + v1_costs[v2] + v2_costs[n]
    v2_first = start_costs[v2] + v2_costs[v1] + v1_costs[n]
    answer = min(v1_first, v2_first)
    print(answer if answer != float("inf") else -1)


main()
