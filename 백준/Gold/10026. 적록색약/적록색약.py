import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def is_frame(x, y, N):
    return 0 <= x < N and 0 <= y < N

def bfs(arr, visited, x, y, N):
    target = arr[y][x]
    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        pos = queue.popleft()
        x = pos[0]
        y = pos[1]

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if (is_frame(nx, ny, N) == False):
                continue
            if (visited[ny][nx] == True):
                continue
            if (arr[ny][nx] != target):
                continue
                
            queue.append((nx, ny))
            visited[ny][nx] = True

def main():
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    real_count = 0
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if (visited[y][x] == True):
                continue
            bfs(arr, visited, x, y, N)
            real_count += 1


    fake_count = 0
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if (arr[y][x] == 'G'):
                arr[y][x] = 'R'
    for y in range(N):
        for x in range(N):
            if (visited[y][x] == True):
                continue
            bfs(arr, visited, x, y, N)
            fake_count += 1

    print(real_count, fake_count)

main()