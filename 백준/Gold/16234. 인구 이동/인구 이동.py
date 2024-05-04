import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(arr, x, y, visited):
    queue = deque([(x, y)])
    pos_list = []
    count = 1
    all_sum = 0

    while queue:
        x, y = queue.popleft()
        pos_list.append((x, y))
        all_sum += arr[y][x]

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) == False or visited[ny][nx] == True:
                continue
            diff = abs(arr[y][x] - arr[ny][nx])
            if L <= diff <= R:
                visited[ny][nx] = True
                count += 1
                queue.append((nx, ny))

    for pos in pos_list:
        x, y = pos
        arr[y][x] = all_sum // count
    return 1 if 1 < count else 0


n = L = R = 0


def solution():
    global n, L, R

    n, L, R = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    day = 0
    while True:
        stop = 0
        visited = [[False] * n for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if visited[y][x] == False:
                    visited[y][x] = True
                    stop += bfs(arr, x, y, visited)
        if stop == 0:
            break
        day += 1

    print(day)


solution()
