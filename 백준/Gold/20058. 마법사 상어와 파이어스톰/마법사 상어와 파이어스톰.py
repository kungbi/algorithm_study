import sys
from copy import deepcopy
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def rotate(arr, point, l):
    point_x, point_y = point

    for i in range(l):
        for j in range(i, l):
            arr[point_y + i][point_x + j], arr[point_y + j][point_x + i] = (
                arr[point_y + j][point_x + i],
                arr[point_y + i][point_x + j],
            )
    for i in range(l):
        for j in range(l // 2):
            arr[point_y + i][point_x + j], arr[point_y + i][point_x + l - 1 - j] = (
                arr[point_y + i][point_x + l - 1 - j],
                arr[point_y + i][point_x + j],
            )


def storm(arr, l):
    for y in range(0, len(arr), l):
        for x in range(0, len(arr[0]), l):
            rotate(arr, (x, y), l)


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y, n):
    return 0 <= x < n and 0 <= y < n


def melt(arr, n):
    result = deepcopy(arr)

    for y in range(n):
        for x in range(n):
            count = 0
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if is_frame(nx, ny, n):
                    if 0 < arr[ny][nx]:
                        count += 1
            if count < 3 and result[y][x] != 0:
                result[y][x] -= 1
    return result


def get_count(arr, visited, start):
    queue = deque([start])
    x, y = start
    visited[y][x] = True

    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if (
                is_frame(nx, ny, len(arr))
                and visited[ny][nx] == False
                and 0 < arr[ny][nx]
            ):
                visited[ny][nx] = True
                queue.append((nx, ny))
    return count


def solution():
    n, q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2**n)]

    storm_list = list(map(int, input().split()))
    for l in storm_list:
        storm(arr, 2**l)
        arr = melt(arr, 2**n)

    print(sum(map(sum, arr)))
    result = 0
    visited = [[False] * (2**n) for _ in range(2**n)]
    for y in range(2**n):
        for x in range(2**n):
            if visited[y][x] == False and 0 < arr[y][x]:
                result = max(result, get_count(arr, visited, (x, y)))
    print(result)


solution()
