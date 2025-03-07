import sys
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def dijkstra(edges, start, v):
    heap = []
    heappush(heap, (0, start))

    costs = [float("inf")] * (v + 1)
    costs[start] = 0

    while heap:
        curr_cost, curr_pos = heappop(heap)

        if costs[curr_pos] < curr_cost:
            continue

        for i, cost in edges[curr_pos]:
            if cost == float("inf"):
                continue

            next_cost = curr_cost + cost
            if next_cost < costs[i]:
                costs[i] = next_cost
                heappush(heap, (next_cost, i))

    return costs


def main():
    v, e = map(int, input().split())
    start = int(input())
    edges = [list() for _ in range(v + 1)]

    for _ in range(e):
        a, b, w = map(int, input().split())
        edges[a].append((b, w))

    costs = dijkstra(edges, start, v)
    for cost in costs[1:]:
        print(cost if cost != float("inf") else "INF")


main()
