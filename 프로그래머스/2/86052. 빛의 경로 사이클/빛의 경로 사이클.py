from collections import defaultdict

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def is_frame(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def f(grid, start, i):
    global dict, visited
    
    n = len(grid)
    m = len(grid[0])
    
    x, y = start
    d = i
    dist = 0
    while True:
        dist += 1
        if grid[y][x] == 'L':
            d = (d - 1) % 4
        elif grid[y][x] == 'R':
            d = (d + 1) % 4
        
        
        nx = x + dxs[d]
        ny = y + dys[d]
        if not is_frame(nx, ny, m, n):
            if nx < 0:
                nx = m - 1
            elif m <= nx:
                nx = 0
            elif ny < 0:
                ny = n - 1
            elif n <= ny:
                ny = 0
        
        # if dict[(x, y, nx, ny, d)] == True:
        #     break
        # dict[(x, y, nx, ny, d)] = True
        if visited[x][y][d] == True:
            break
        visited[x][y][d] = True
        x, y = nx, ny
        
    if x == start[0] and y == start[1]:
        return dist - 1
        
        
    

def solution(grid):
    global dict, visited
    
    n = len(grid)
    m = len(grid[0])
    dict = defaultdict(bool)
    visited = [[[0] * 4 for _ in range(500)] for _ in range(500)]
    
    answer = []
    for y in range(n):
        for x in range(m):
            for i in range(4):
                tmp = f(grid, (x, y), i)
                if tmp != 0:
                    answer.append(tmp)
    answer.sort()
    return answer
        