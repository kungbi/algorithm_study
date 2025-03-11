import sys
from collections import defaultdict
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def solution(edges, start, n):
    costs = [float("inf")] * (n + 1)

    heap = []
    heappush(heap, (0, start))
    costs[start] = 0

    while heap:
        curr_cost, curr_node = heappop(heap)

        if costs[curr_node] < curr_cost:
            continue

        for next_node, next_cost in edges[curr_node]:
            if curr_cost + next_cost < costs[next_node]:
                costs[next_node] = curr_cost + next_cost
                heappush(heap, (curr_cost + next_cost, next_node))

    return costs


def main():
    n, m, x = map(int, input().split())
    edges = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))

    back_costs = solution(edges, x, n)

    result = 0
    for start_node in range(1, n + 1):
        if start_node == x:
            continue

        costs = solution(edges, start_node, n)
        result = max(result, costs[x] + back_costs[start_node])

    return result


print(main())
