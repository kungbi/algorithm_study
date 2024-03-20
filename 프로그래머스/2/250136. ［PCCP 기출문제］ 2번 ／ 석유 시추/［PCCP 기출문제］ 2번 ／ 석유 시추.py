from collections import deque

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

oil_list = []
visited = []
n = m = result = 0


def is_frame(x, y):
    return 0 <= x < m and 0 <= y < n


def counter(land, start):
    global visited, oil_list, result

    x, y = start
    queue = deque([(x, y)])
    visited[y][x] = True
    min_x = float('inf')
    max_x = float('-inf')
    
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        
        min_x = min(min_x, x)
        max_x = max(max_x, x)

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) and visited[ny][nx] == False and land[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny))

    for i in range(min_x, max_x + 1):
        oil_list[i] += count
        result = max(result, oil_list[i])


def solution(land):
    global oil_list, visited, m, n

    n = len(land)
    m = len(land[0])
    oil_list = [0] * m
    visited = [[False] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and visited[y][x] == False:
                counter(land, (x, y))
    return result
