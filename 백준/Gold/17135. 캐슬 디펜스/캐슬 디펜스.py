import sys
from collections import deque
from copy import deepcopy
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


def down(arr):
    for y in range(n - 1, 0, -1):
        for x in range(m):
            arr[y][x] = arr[y - 1][x]
    for x in range(m):
        arr[0][x] = 0


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < m and 0 <= y < n


def find_enemy(arr, pos):
    result = []
    queue = deque()
    queue.append((pos[0], pos[1], 1))
    visited = [[False] * m for _ in range(n)]
    visited[pos[1]][pos[0]] = True

    while queue:
        x, y, dist = queue.popleft()

        if d < dist:
            break
        if arr[y][x] == 1:
            result.append((x, y))

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append((nx, ny, dist + 1))
    return result


def shot(arr, archer):
    kill = 0

    selected_enemy = []
    for col in archer:
        enemy_list = find_enemy(arr, (col, n - 1))
        if enemy_list:
            selected_enemy.append(enemy_list[0])

    selected_enemy = set(selected_enemy)
    for enemy in selected_enemy:
        x, y = enemy
        arr[y][x] = 0
    return len(selected_enemy)


def calc(arr, archer):
    kill = 0

    for _ in range(n):
        kill += shot(arr, archer)
        down(arr)
    return kill


n = m = d = 0
result = 0


def solution():
    global n, m, d

    n, m, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    archer_lsit = combinations(range(m), 3)
    result = 0
    for archer in archer_lsit:
        arr_tmp = deepcopy(arr)
        result = max(result, calc(arr_tmp, archer))
    print(result)


solution()
