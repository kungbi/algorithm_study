import sys
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


def is_frame(x, y):
    global n, m
    return 0 <= x < m and 0 <= y < n


def determine_order(board, dir, red_pos, blue_pos):
    # 움직일 순서 정하기
    order = ["R", "B"]
    if dir == 0:
        for i in range(red_pos[0]):
            if board[red_pos[1]][i] == "B":
                order = ["B", "R"]
    if dir == 1:
        for i in range(red_pos[1]):
            if board[i][red_pos[0]] == "B":
                order = ["B", "R"]
    if dir == 2:
        for i in range(m - 1, red_pos[0], -1):
            if board[red_pos[1]][i] == "B":
                order = ["B", "R"]
    if dir == 3:
        for i in range(n - 1, red_pos[1], -1):
            if board[i][red_pos[0]] == "B":
                order = ["B", "R"]
    return order


def move(board, dir, color, red_pos, blue_pos):
    pos = None
    if color == "R":
        pos = red_pos
    elif color == "B":
        pos = blue_pos
    x, y = pos
    board[y][x] = "."

    dx, dy = dxs[dir], dys[dir]
    nx, ny = x + dx, y + dy
    while is_frame(nx, ny) and board[ny][nx] == ".":
        x, y = nx, ny
        nx, ny = x + dx, y + dy

    nx, ny = x + dx, y + dy
    if is_frame(nx, ny) and board[ny][nx] == "O":
        x, y = nx, ny
    else:
        board[y][x] = color
    if color == "R":
        red_pos[0] = x
        red_pos[1] = y
    elif color == "B":
        blue_pos[0] = x
        blue_pos[1] = y


def incline(board, dir, red_pos, blue_pos):
    """
    0: left
    1: up
    2: right
    3: down
    """

    order = determine_order(board, dir, red_pos, blue_pos)
    for color in order:
        move(board, dir, color, red_pos, blue_pos)

    if blue_pos == dest_pos:
        return -1
    elif red_pos == dest_pos:
        return 1
    return 0


def f(board, count, red_pos, blue_pos):
    global answer

    if 10 < count:
        return
    for i in range(4):
        tmp_board = deepcopy(board)
        tmp_red_pos = deepcopy(red_pos)
        tmp_blue_pos = deepcopy(blue_pos)
        result = incline(tmp_board, i, tmp_red_pos, tmp_blue_pos)
        if result == 1:
            answer = min(answer, count)
            return
        elif result == -1:
            continue
        elif tmp_red_pos == red_pos and tmp_blue_pos == blue_pos:
            continue
        f(tmp_board, count + 1, tmp_red_pos, tmp_blue_pos)


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]
n = m = 0
answer = float("inf")
dest_pos = ()


def solution():
    global dest_pos, n, m

    red_pos = ()
    blue_pos = ()
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if board[y][x] == "R":
                red_pos = [x, y]
            elif board[y][x] == "B":
                blue_pos = [x, y]
            elif board[y][x] == "O":
                dest_pos = [x, y]

    f(board, 1, red_pos, blue_pos)
    print(answer if answer != float("inf") else -1)


solution()
