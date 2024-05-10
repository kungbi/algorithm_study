def solution(board, skill_list):
    n = len(board)
    m = len(board[0])
    
    prefix_arr = [[0] * (m + 1) for _ in range(n + 1)]
    for skill in skill_list:
        type, r1, c1, r2, c2, degree = skill
        t = (type * 2) - 3
        prefix_arr[r1][c1] += t * degree
        prefix_arr[r2 + 1][c1] += t * degree * -1
        prefix_arr[r1][c2 + 1] += t * degree * -1
        prefix_arr[r2 + 1][c2 + 1] += t * degree
        
    
    # 세로 
    for x in range(m):
        for y in range(1, n):
            prefix_arr[y][x] += prefix_arr[y-1][x]
    
    for y in range(n):
        for x in range(1, m):
            prefix_arr[y][x] += prefix_arr[y][x-1]

    answer = 0
    for y in range(n):
        for x in range(m):
            board[y][x] += prefix_arr[y][x]
            if 0 < board[y][x]:
                answer += 1
    return answer