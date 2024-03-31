import sys
from copy import deepcopy
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < m and 0 <= y < n


def fill(arr, visited, start):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) and visited[ny][nx] == False and arr[ny][nx] != 0:
                visited[ny][nx] = True
                queue.append((nx, ny))


def get_iceberg_count(arr):
    visited = [[False] * m for _ in range(n)]
    count = 0

    for y in range(n):
        for x in range(m):
            if arr[y][x] != 0 and visited[y][x] == False:
                visited[y][x] = True
                fill(arr, visited, (x, y))
                count += 1
    return count


def melt(arr):
    arr_copy = deepcopy(arr)

    for y in range(n):
        for x in range(m):
            count = 0
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if is_frame(nx, ny) and arr[ny][nx] == 0:
                    count += 1
            arr_copy[y][x] = max(0, arr[y][x] - count)
    return arr_copy


n = m = 0


def solution():
    global n, m

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    year = 0
    while 1 == get_iceberg_count(arr):
        year += 1
        arr = melt(arr)

    if get_iceberg_count(arr) == 0:
        print(0)
    else:
        print(year)


solution()
