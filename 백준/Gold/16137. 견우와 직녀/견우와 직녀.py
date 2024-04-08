import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]


def is_frame(x, y):
    return 0 <= x < n and 0 <= y < n


def get_dist(arr):
    queue = deque([(0, 0, 0, 0)])
    visited = [[[False, False] for _ in range(n)] for _ in range(n)]
    visited[0][0][0] = True
    visited[0][0][1] = True

    while queue:
        x, y, dist, bridge = queue.popleft()
        if x == n - 1 and y == n - 1:
            return dist

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if (
                is_frame(nx, ny)
                and 0 <= arr[ny][nx]
                and visited[ny][nx][bridge] == False
            ):
                if arr[ny][nx] == 1:
                    visited[ny][nx][bridge] = True
                    queue.append((nx, ny, dist + 1, bridge))
                elif 2 <= arr[ny][nx] and arr[y][x] == 1:
                    if (dist + 1) % arr[ny][nx] == 0:
                        queue.append((nx, ny, dist + 1, bridge))
                    else:
                        queue.append((x, y, dist + 1, bridge))
                elif arr[ny][nx] == 0 and bridge == 0:
                    if (dist + 1) % m == 0:
                        queue.append((nx, ny, dist + 1, bridge + 1))
                    else:
                        queue.append((x, y, dist + 1, bridge))
    return -1


def is_corner(arr, x, y):
    clif_count = 0
    floor_count = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if is_frame(nx, ny):
            if arr[ny][nx] == 0 or 2 <= arr[ny][nx]:
                clif_count += 1
            elif 2 <= arr[ny][nx]:
                floor_count += 1
    if 3 <= clif_count:
        return True
    elif clif_count == 2 and floor_count == 2:
        return True
    return False


n = m = 0


def solution():
    global n, m

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dist = get_dist(arr)
    print(dist)


solution()
