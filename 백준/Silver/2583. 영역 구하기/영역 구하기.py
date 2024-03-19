import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def fill(arr, pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    for y in range(m):
        for x in range(n):
            if x1 <= x < x2 and y1 <= y < y2:
                arr[y][x] += 1


n = m = result = 0

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(arr, pos):
    global result

    x, y = pos
    arr[y][x] = 1
    result += 1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if is_frame(nx, ny) and arr[ny][nx] == 0:
            dfs(arr, (nx, ny))


def solution():
    global n, m, result

    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        fill(arr, (x1, y1), (x2, y2))

    result_list = []
    for y in range(m):
        for x in range(n):
            if arr[y][x] == 0:
                result = 0
                dfs(arr, (x, y))
                result_list.append(result)
    result_list.sort()
    print(len(result_list))
    print(*result_list)


solution()
