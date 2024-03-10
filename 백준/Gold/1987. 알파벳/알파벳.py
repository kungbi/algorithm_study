import sys


def input():
    return sys.stdin.readline().rstrip()


dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def is_frame(x, y):
    return 0 <= x < c and 0 <= y < r


def to_index(c):
    return ord(c) - ord("A")


def dfs(arr, curr, visited):
    global result

    x, y, d = curr
    result = max(result, d)
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if is_frame(nx, ny) == False:
            continue

        index = to_index(arr[ny][nx])
        if visited[index] == False:
            visited[index] = True
            dfs(arr, (nx, ny, d + 1), visited)
            visited[index] = False


r = c = 0


def solution():
    global r, c, result
    r, c = map(int, input().split())
    arr = [list(input()) for _ in range(r)]

    result = 0
    visited = [False] * 26
    visited[to_index(arr[0][0])] = True
    dfs(arr, (0, 0, 1), visited)
    print(result)


solution()
