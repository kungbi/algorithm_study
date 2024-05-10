from collections import deque


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y, n):
    return 0 <= x < n and 0 <= y < n


def bfs(board):
    n = len(board)
    cost_board = [[float("inf")] * n for _ in range(n)]
    cost_board[0][0] = -500
    queue = deque([(0, 0, -500)])

    while queue:
        x, y, cost = queue.popleft()
        cost = cost_board[y][x] + 500

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            nc = cost + 100
            while is_frame(nx, ny, n) and board[ny][nx] == 0:
                if nc <= cost_board[ny][nx]:
                    cost_board[ny][nx] = nc
                    queue.append((nx, ny, nc))
                nx += dx
                ny += dy
                nc += 100
    return cost_board[n - 1][n - 1]


def solution(board):
    return bfs(board)
