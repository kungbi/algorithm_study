import sys
sys.setrecursionlimit(10**6)

n = None
visited = None
sheep_max = 0

def dfs(info, edges_arr, curr, sheep, wolf):
    global n, visited, sheep_max
    
    if info[curr] == 0:
        sheep += 1
    else:
        wolf += 1
    
    sheep_max = max(sheep_max, sheep)

    if sheep <= wolf:
        return sheep
    
    for p_i in range(n):
        for c_i in range(n):
            if edges_arr[p_i][c_i] == 1 and visited[p_i] == True and visited[c_i] == False:
                visited[c_i] = True
                dfs(info, edges_arr, c_i, sheep, wolf)
                visited[c_i] = False
    return sheep
    

def solution(info, edges):
    global n, visited, sheep_max
    
    n = len(info)
    visited = [False] * n
    visited[0] = True
    
    edges_arr = [[0] * n for _ in range(n)]
    for edge in edges:
        p, c = edge
        edges_arr[p][c] = 1
    
    dfs(info, edges_arr, 0, 0, 0)
    return sheep_max
    
    
    