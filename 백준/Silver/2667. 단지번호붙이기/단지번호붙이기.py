import sys
def input():
    return sys.stdin.readline().rstrip()

n = None

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def is_frame(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(arr, visited, pos):
    x, y = pos
    
    cnt = 1
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if is_frame(nx, ny) and visited[ny][nx] == False and arr[ny][nx] == 1:
            visited[ny][nx] = True
            cnt += dfs(arr, visited, (nx, ny))
    return cnt

def solution():
    global n

    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    result_list = []
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 1 and visited[y][x] == False:
                visited[y][x] = True
                result_list.append(dfs(arr, visited, (x, y)))
    print(len(result_list))
    for num in sorted(result_list):
        print(num)
        
solution()