import sys
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def dijkstra(arr, costs, departure, arrival, n):
    heap = [(0, departure)]
    visited = [False] * (n + 1)

    while heap:
        curr_cost, curr_pos = heappop(heap)

        if visited[curr_pos]:
            continue
        visited[curr_pos] = True

        for i in range(1, n + 1):
            if costs[curr_pos][i] == -1:
                continue

            next_cost = costs[curr_pos][i] + curr_cost
            if next_cost < arr[i]:
                arr[i] = next_cost
                heappush(heap, (next_cost, i))

    return arr[arrival]


def main():
    n = int(input())
    m = int(input())

    costs = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        costs[a][b] = min(costs[a][b], c)

    departure, arrival = map(int, input().split())

    arr = [float("inf")] * (n + 1)
    arr[departure] = 0
    print(dijkstra(arr, costs, departure, arrival, n))


main()
