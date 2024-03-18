import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < c and 0 <= y < r


def bfs(arr, start, water_list, end):
    water_queue = deque(water_list)

    player_queue = deque()
    player_queue.append((start[0], start[1], 0))
    visited = [[False] * c for _ in range(r)]
    visited[start[1]][start[0]] = True

    while player_queue:

        i = 0
        water_queue_len = len(water_queue)
        while i < water_queue_len:
            i += 1
            x, y = water_queue.popleft()

            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if is_frame(nx, ny) and arr[ny][nx] == ".":
                    arr[ny][nx] = "*"
                    water_queue.append((nx, ny))

        i = 0
        player_queue_len = len(player_queue)
        while i < player_queue_len:
            i += 1
            x, y, d = player_queue.popleft()

            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if is_frame(nx, ny) and arr[ny][nx] == "D":
                    return d + 1
                if is_frame(nx, ny) and arr[ny][nx] == "." and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    player_queue.append((nx, ny, d + 1))
    return -1


r = c = 0


def solution():
    global r, c
    r, c = map(int, input().split())
    arr = [list(input()) for _ in range(r)]

    water_list = []
    start = None
    end = None
    for y in range(r):
        for x in range(c):
            if arr[y][x] == "*":
                water_list.append((x, y))
            if arr[y][x] == "S":
                start = (x, y)
            if arr[y][x] == "D":
                end = (x, y)
    result = bfs(arr, start, water_list, end)
    if result == -1:
        result = "KAKTUS"
    print(result)


solution()
