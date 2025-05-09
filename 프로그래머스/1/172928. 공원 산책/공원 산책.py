dxs = [-1, 0, 1, 0]
dys = [0 ,-1, 0, 1]

def is_frame(x, y, n, m):
    return 0 <= x < m and 0 <= y < n

def convert(dir):
    if dir == 'E':
        return 2
    if dir == 'W':
        return 0
    if dir == 'N':
        return 1
    return 3

def move(park, x, y, dis, dir, n, m):
    backup_x = x
    backup_y = y
    
    for _ in range(dis):
        dx = dxs[convert(dir)]
        dy = dys[convert(dir)]
        
        nx = x + dx
        ny = y + dy

        if not is_frame(nx, ny, n, m):
            return [backup_x, backup_y]
        if park[ny][nx] == 'X':
            return [backup_x, backup_y]

        x, y = nx, ny
    return [x, y]
    

def solution(park, routes):
    n = len(park)
    m = len(park[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x = j
                y = i
        
    for command in routes:
        dir, dis = command.split()
        dis = int(dis)
        
        x, y = move(park, x, y, dis, dir, n, m)
    return [y, x]
        
        
    