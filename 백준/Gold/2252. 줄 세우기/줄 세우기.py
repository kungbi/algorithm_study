import sys
from collections import defaultdict
from collections import deque
from typing import Deque

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def solution(edges, in_degree):
    queue = deque()
    for i in range(1, len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    answer = []
    while queue:
        node = queue.popleft()
        answer.append(node)
        for n_node in edges[node]:
            in_degree[n_node] -= 1
            if in_degree[n_node] == 0:
                queue.append(n_node)
    return answer


def main():
    n, m = map(int, input().split())
    edges = defaultdict(list)

    in_degree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        in_degree[b] += 1

    print(*solution(edges, in_degree))


main()
