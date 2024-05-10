import sys
from heapq import heappop
from heapq import heappush
from collections import defaultdict

MAX = sys.maxsize


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, m = map(int, input().split())

    edges = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    cost_array = [MAX] * (n + 1)
    heap = [(0, 1)]
    cost_array[1] = 0
    while heap:
        cost, node = heappop(heap)
        if cost_array[node] < cost:
            continue

        for n_node, n_cost in edges[node]:
            if cost + n_cost < cost_array[n_node]:
                cost_array[n_node] = cost + n_cost
                heappush(heap, (cost + n_cost, n_node))
    print(cost_array[n])


solution()
