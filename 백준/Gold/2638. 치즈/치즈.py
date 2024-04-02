import sys
from collections import deque
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


def melt(arr):
    arr_copy = deepcopy(arr)
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                count = 0
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy

                    if arr[ny][nx] == 2:
                        count += 1
                if 2 <= count:
                    arr_copy[y][x] = 2
    return arr_copy


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < m and 0 <= y < n


def air(arr):
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    arr[0][0] = 2

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if (
                is_frame(nx, ny)
                and (arr[ny][nx] == 0 or arr[ny][nx] == 2)
                and visited[ny][nx] == False
            ):
                visited[ny][nx] = True
                arr[ny][nx] = 2
                queue.append((nx, ny))


def check(arr):
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                return True
    return False


n = m = 0


def solution():
    global n, m

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    air(arr)
    result = 0
    while check(arr):
        arr = melt(arr)
        air(arr)
        result += 1
    print(result)


solution()
