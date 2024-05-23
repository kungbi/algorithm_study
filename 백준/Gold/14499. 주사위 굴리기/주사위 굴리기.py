import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [0, 0, 0, -1, 1]
dys = [0, 1, -1, 0, 0]


def left(dice_x, dice_y):
    num = dice_x.pop()
    dice_x.appendleft(num)
    dice_y[-1] = dice_x[-1]
    dice_y[1] = dice_x[1]


def right(dice_x, dice_y):
    num = dice_x.popleft()
    dice_x.append(num)
    dice_y[-1] = dice_x[-1]
    dice_y[1] = dice_x[1]


def up(dice_x, dice_y):
    num = dice_y.pop()
    dice_y.appendleft(num)
    dice_x[-1] = dice_y[-1]
    dice_x[1] = dice_y[1]


def down(dice_x, dice_y):
    num = dice_y.popleft()
    dice_y.append(num)
    dice_x[-1] = dice_y[-1]
    dice_x[1] = dice_y[1]


def is_frame(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def solution():
    n, m, x, y, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dice_x = deque([0] * 4)
    dice_y = deque([0] * 4)

    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    command_list = list(map(int, input().split()))
    for command in command_list:
        nx = x + dxs[command]
        ny = y + dys[command]
        if not is_frame(nx, ny, n, m):
            continue

        x, y = nx, ny
        if command == 1:
            right(dice_x, dice_y)
        elif command == 2:
            left(dice_x, dice_y)
        elif command == 3:
            up(dice_x, dice_y)
        elif command == 4:
            down(dice_x, dice_y)

        if arr[x][y] == 0:
            arr[x][y] = dice_x[3]
        else:
            dice_x[3] = arr[x][y]
            dice_y[3] = arr[x][y]
            arr[x][y] = 0
        print(dice_x[1])


solution()
