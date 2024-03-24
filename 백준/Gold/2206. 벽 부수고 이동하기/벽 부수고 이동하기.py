import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def is_frame(x, y):
    return 0 <= x < m and 0 <= y < n


def bfs(arr):
    queue = deque([(0, 0, 1, 0)])
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    visited[0][0] = [True, True]

    while queue:
        x, y, d, t = queue.popleft()

        if x == m - 1 and y == n - 1:
            return d

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if not is_frame(nx, ny):
                continue

            if arr[ny][nx] == 0 and visited[ny][nx][t] == False:
                visited[ny][nx][t] = True
                queue.append((nx, ny, d + 1, t))
            elif arr[ny][nx] == 1 and t == 0 and visited[ny][nx][t] == False:
                visited[ny][nx][t] = True
                queue.append((nx, ny, d + 1, 1))


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]
n = m = 0


def solution():
    global n, m

    n, m = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    result = bfs(arr)
    print(result if result else -1)


solution()
