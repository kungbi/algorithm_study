import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]
dwall = [1, 2, 4, 8]


def is_frame(x, y):
    return 0 <= x < m and 0 <= y < n


def is_available(arr, x, y, nx, ny):
    if arr[ny][nx] & 1:  # 서
        tx = nx + dxs[0]
        ty = ny + dys[0]
        if is_frame(tx, ty) and x == tx and y == ty:
            return False
    if arr[ny][nx] & 2:  # 북
        tx = nx + dxs[1]
        ty = ny + dys[1]
        if is_frame(tx, ty) and x == tx and y == ty:
            return False
    if arr[ny][nx] & 4:  # 동
        tx = nx + dxs[2]
        ty = ny + dys[2]
        if is_frame(tx, ty) and x == tx and y == ty:
            return False
    if arr[ny][nx] & 8:  # 남
        tx = nx + dxs[3]
        ty = ny + dys[3]
        if is_frame(tx, ty) and x == tx and y == ty:
            return False
    return True


def get_count(arr, x, y, visited, rooms_arr, num):
    queue = deque([(x, y)])
    visited[y][x] = True

    pos_list = []
    count = 1
    while queue:
        x, y = queue.popleft()
        pos_list.append((x, y))
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if (
                is_frame(nx, ny)
                and visited[ny][nx] == False
                and is_available(arr, x, y, nx, ny)
            ):
                visited[ny][nx] = True
                count += 1
                queue.append((nx, ny))
    for x, y in pos_list:
        rooms_arr[y][x] = [num, count]
    return count


def get_biggest_count(arr):
    visited = [[False] * m for _ in range(n)]
    max_v = 0
    for y in range(n):
        for x in range(m):
            if visited[y][x] == False:
                max_v = max(max_v, get_count(arr, x, y, visited))
    return max_v


n = m = 0


def solution():
    global n, m
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    rooms_list = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0
    max_v = 0
    num = 0
    for y in range(n):
        for x in range(m):
            if visited[y][x] == False:
                count += 1
                max_v = max(max_v, get_count(arr, x, y, visited, rooms_list, num))
                num += 1

    biggest_count = 0
    for y in range(n):
        for x in range(m):
            if 0 < arr[y][x]:
                for i in range(4):
                    if arr[y][x] & dwall[i]:
                        nx = x + dxs[i]
                        ny = y + dys[i]
                        if (
                            is_frame(nx, ny)
                            and rooms_list[y][x][0] != rooms_list[ny][nx][0]
                        ):
                            biggest_count = max(
                                biggest_count,
                                rooms_list[y][x][1] + rooms_list[ny][nx][1],
                            )

    print(count)
    print(max_v)
    print(biggest_count)


solution()
