import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]


def is_frame(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def solution(arr, n, m, k):
    queue = deque([(0, 0, 1, 0)])
    visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while queue:
        x, y, moved, broke = queue.popleft()
        if x == m - 1 and y == n - 1:
            return moved

        daytime = moved % 2
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not is_frame(nx, ny, n, m):
                continue

            if arr[ny][nx] == 1 and broke < k and visited[ny][nx][broke + 1] == 0:
                if daytime == 1:
                    visited[ny][nx][broke + 1] = moved
                    queue.append((nx, ny, moved + 1, broke + 1))
                elif daytime == 0:
                    visited[y][x][broke] = moved
                    queue.append((x, y, moved + 1, broke))

            if arr[ny][nx] == 0 and visited[ny][nx][broke] == 0:
                visited[ny][nx][broke] = moved
                queue.append((nx, ny, moved + 1, broke))

    return -1


def main():
    n, m, k = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(n)]

    print(solution(arr, n, m, k))


main()
