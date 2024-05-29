import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def is_frame(x, y, n):
    return 0 <= x < n and 0 <= y < n


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def dijkstra(graph, dist, n):
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_frame(nx, ny, n) and dist[y][x] + graph[ny][nx] < dist[ny][nx]:
                dist[ny][nx] = dist[y][x] + graph[ny][nx]
                queue.append((nx, ny))


def solution():
    global answer

    i = 1
    while True:
        n = int(input())
        if n == 0:
            break

        answer = sys.maxsize
        graph = [list(map(int, input().split())) for _ in range(n)]
        dist = [[sys.maxsize] * n for _ in range(n)]
        dist[0][0] = graph[0][0]

        dijkstra(graph, dist, n)
        print("""Problem {}: {}""".format(i, dist[n - 1][n - 1]))
        i += 1


solution()
