import sys
from collections import deque
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution(arr, in_degree, n):
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        n_node = arr[node]
        in_degree[n_node] -= 1
        if in_degree[n_node] == 0:
            queue.append(n_node)
    return result


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [0] + list(map(int, input().split()))
        in_degree = [0] * (n + 1)
        for i in range(1, n + 1):
            in_degree[arr[i]] += 1
        result = solution(arr, in_degree, n)
        print(len(result))


main()
