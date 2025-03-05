import sys


def input():
    return sys.stdin.readline().rstrip()


# 0: 가로, 1: 세로, 2: 대각
dxs = [[1, 1], [0, 1], [1, 0, 1]]
dys = [[0, 1], [1, 1], [0, 1, 1]]
dirs = [[0, 2], [1, 2], [0, 1, 2]]

dp = None


def is_frame(x, y, n):
    return 0 <= x < n and 0 <= y < n


def is_available(arr, x, y, dir):
    if dir == 0:
        return arr[y][x] != 1 and arr[y][x - 1] != 1
    if dir == 1:
        return arr[y][x] != 1 and arr[y - 1][x] != 1
    if dir == 2:
        return (
            arr[y][x] != 1
            and arr[y - 1][x] != 1
            and arr[y][x - 1] != 1
            and arr[y - 1][x - 1] != 1
        )


def f(arr, dir, pos, n):
    x, y = pos

    if x == n - 1 and y == n - 1:
        return 1

    if dp[y][x][dir] != -1:
        return dp[y][x][dir]

    result = 0
    for dx, dy, ndir in zip(dxs[dir], dys[dir], dirs[dir]):
        nx, ny = x + dx, y + dy
        if is_frame(nx, ny, n) == False:
            continue
        if is_available(arr, nx, ny, ndir) == 0:
            continue

        result += f(arr, ndir, (nx, ny), n)

    dp[y][x][dir] = result
    return result


def main():
    global dp

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
    return f(arr, 0, (1, 0), n)


print(main())
