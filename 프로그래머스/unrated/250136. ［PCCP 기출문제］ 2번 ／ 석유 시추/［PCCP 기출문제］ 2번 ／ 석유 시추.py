from collections import deque

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
result = []
def is_frame(x, y, n, m):
    return 0 <= x < m and 0 <= y < n

def bfs(land, visited, dp, pos):
    min_x, max_x = float('inf'), 0
    queue = deque([pos])
    n = len(land)
    m = len(land[0])
    count = 0
    visited_x = [0] * m
    
    while queue:
        curr_pos = queue.popleft()
        x, y = curr_pos
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        visited[y][x] = True
        visited_x[x] = True
        count += 1
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny, n, m) and land[ny][nx] == 1:
                if visited[ny][nx] == True:
                    continue
                queue.append((nx, ny))
                visited[ny][nx] = True
                
    result.append((min_x,max_x, count))


def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[0] * m for _ in range(n)]
    dp = [0] * m
    for y in range(n):
        for x in range(m):
            if visited[y][x] == False and land[y][x] == 1:
                bfs(land, visited, dp, (x, y))
    for t in result:
        start, end, c = t
        for i in range(start, end+1):
            dp[i] += c
    return max(dp)