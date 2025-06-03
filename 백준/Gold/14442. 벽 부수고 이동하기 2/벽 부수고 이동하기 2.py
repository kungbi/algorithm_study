import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]


def is_frame(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def solution(arr, k):
    n = len(arr)
    m = len(arr[0])

    queue = deque([((0, 0), 1, 0)])
    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0] = [True] * (k + 1)

    while queue:
        (x, y), moved, broken = queue.popleft()
        if x == m - 1 and y == n - 1:
            return moved

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not is_frame(nx, ny, n, m):
                continue
            if visited[ny][nx][broken]:
                continue

            if arr[ny][nx] == 1:
                if broken == k:
                    continue
                visited[ny][nx][broken] = True
                queue.append(((nx, ny), moved + 1, broken + 1))
                continue

            visited[ny][nx][broken] = True
            queue.append(((nx, ny), moved + 1, broken))

    return -1


def main():
    n, m, k = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    print(solution(arr, k))


main()
