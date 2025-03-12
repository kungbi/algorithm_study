import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution(edges, start_node, v):
    queue = deque([(start_node, 0)])
    visited = [False] * (v + 1)
    visited[start_node] = True
    costs = []

    while queue:
        node, cost = queue.popleft()
        moved = False

        for next_node, next_cost in edges[node]:
            if visited[next_node]:
                continue

            moved = True
            queue.append((next_node, cost + next_cost))
            visited[next_node] = True

        if moved == False:
            costs.append((node, cost))

    return costs


def main():
    v = int(input())
    edges = defaultdict(list)

    for _ in range(v):
        line = tuple(map(int, input().split()))
        start_node = line[0]

        i = 1
        while line[i] != -1:
            edges[start_node].append((line[i], line[i + 1]))
            i += 2

    costs = solution(edges, 1, v)
    start_node, _ = max(costs, key=lambda x: x[1])

    _, result = max(solution(edges, start_node, v), key=lambda x: x[1])
    return result


print(main())
