import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def calc_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def f(merged_list, edges):
    for i in range(len(merged_list)):
        for j in range(len(merged_list)):
            if i == j:
                continue

            if calc_dist(merged_list[i], merged_list[j]) <= 1000:
                edges[i].append(j)


def is_available(edges, n):
    queue = deque([0])
    visited = [False] * (n + 2)
    visited[0] = True

    while queue:
        curr = queue.popleft()
        for next in edges[curr]:
            if visited[next] == False:
                visited[next] = True
                queue.append(next)

    if visited[-1] == True:
        return True
    return False


def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        home = tuple(map(int, input().split()))
        store_list = []

        for _ in range(n):
            store_list.append(tuple(map(int, input().split())))
        dest = tuple(map(int, input().split()))

        edges = defaultdict(list)
        f([home] + store_list + [dest], edges)
        print("happy" if len(edges) and is_available(edges, n) else "sad")


solution()
