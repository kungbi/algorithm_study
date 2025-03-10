import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def solution(edges, curr_node, visited, cost, records):
    records.append((curr_node, cost))

    for next_node, next_cost in edges[curr_node]:
        if visited[next_node] == True:
            continue

        visited[next_node] = True
        solution(edges, next_node, visited, cost + next_cost, records)


def main():
    n = int(input())
    edges = defaultdict(list)

    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    visited = [False] * (n + 1)
    visited[1] = True
    records = []
    solution(edges, 1, visited, 0, records)

    start_node, _ = max(records, key=lambda x: x[1])
    visited = [False] * (n + 1)
    visited[start_node] = True
    records = []
    solution(edges, start_node, visited, 0, records)

    end_node, result = max(records, key=lambda x: x[1])

    return result


print(main())
