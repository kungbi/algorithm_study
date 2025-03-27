import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution(edges, in_degree):
    queue = deque()
    for idx in range(1, len(in_degree)):
        if in_degree[idx] == 0:
            queue.append(idx)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for n_node in edges[node]:
            in_degree[n_node] -= 1
            if in_degree[n_node] == 0:
                queue.append(n_node)
    return result


def main():
    n, m = map(int, input().split())
    edges = defaultdict(list)
    in_degree = [0] * (n + 1)
    for _ in range(m):
        arr = list(map(int, input().split()))
        for i in range(1, len(arr) - 1):
            if arr[i + 1] in edges[arr[i]]:
                continue
            edges[arr[i]].append(arr[i + 1])
            in_degree[arr[i + 1]] += 1

    answer = solution(edges, in_degree)
    if not answer:
        print(0)
        return
    if len(answer) != n:
        print(0)
        return
    for num in answer:
        print(num)


main()
