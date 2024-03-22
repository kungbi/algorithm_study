import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def is_frame(x, y):
    return 0 <= x < n and 0 <= y < n


def get_distance(arr, start):
    global n

    x, y = start
    num = arr[y][x]
    queue = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True

    while queue:
        x, y, d = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) and visited[ny][nx] == False:
                if arr[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((nx, ny, d + 1))
                elif arr[ny][nx] != num:
                    return d


def fill_map(arr, start, num):
    global n

    x, y = start
    queue = deque([(x, y)])
    arr[y][x] = num

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) and arr[ny][nx] == 1:
                arr[ny][nx] = num
                queue.append((nx, ny))


n = 0
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def solution():
    global n

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    num = 2
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 1:
                fill_map(arr, (x, y), num)
                num += 1
                break

    result = float("inf")
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 0:
                continue
            count = get_distance(arr, (x, y))
            result = min(result, count if count else float("inf"))
    print(result)


solution()
