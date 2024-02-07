def dfs(edges, curr, visited, n):
    moved = 0
    for i in range(1, n + 1):
        if edges[curr][i] == True and visited[i] == False:
            visited[i] = True
            moved += dfs(edges, i, visited, n) + 1
    return moved

def solution(n, results):
    edges_win = [[False] * (n + 1) for _ in range(n + 1)]
    edges_lose = [[False] * (n + 1) for _ in range(n + 1)]
    
    for result in results:
        edges_win[result[0]][result[1]] = True
        edges_lose[result[1]][result[0]] = True
    
    answer = 0
    for i in range(1, n + 1):
        result = 0
        visited = [False] * (n + 1)
        result += dfs(edges_win, i, visited, n)
        visited = [False] * (n + 1)
        result += dfs(edges_lose, i, visited, n)
        if result == n - 1:
            answer += 1
    return answer