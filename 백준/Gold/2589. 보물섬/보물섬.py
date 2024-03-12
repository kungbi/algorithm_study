import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < m and 0 <= y < n


def bfs(arr, start):
    global result

    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * m for _ in range(n)]
    visited[start[1]][start[0]] = True

    while queue:
        x, y, d = queue.popleft()
        result = max(result, d)

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) and visited[ny][nx] == False and arr[ny][nx] == "L":
                visited[ny][nx] = True
                queue.append((nx, ny, d + 1))


n = m = result = 0


def solution():
    global n, m, result

    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    list_l = []
    for y in range(n):
        for x in range(m):
            if arr[y][x] == "L":
                list_l.append((x, y))

    for l in list_l:
        bfs(arr, l)
    print(result)


solution()
