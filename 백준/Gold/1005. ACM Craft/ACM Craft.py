import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def tropoly_sort(in_degree, edges, n):
    queue = deque()
    for node in range(1, n + 1):
        if in_degree[node] == 0:
            queue.append(node)

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
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = [0] + list(map(int, input().split()))
        edges = defaultdict(list)
        in_degree = [0] * (n + 1)
        for _ in range(k):
            x, y = map(int, input().split())
            edges[x].append(y)
            in_degree[y] += 1
        w = int(input())

        sorted_nodes_queue = deque(tropoly_sort(in_degree, edges, n))
        dp = [0] * (n + 1)

        while sorted_nodes_queue:
            node = sorted_nodes_queue.popleft()
            cost = arr[node]

            for n_node in edges[node]:
                dp[n_node] = max(dp[n_node], dp[node] + cost)
        print(dp[w] + arr[w])


main()
