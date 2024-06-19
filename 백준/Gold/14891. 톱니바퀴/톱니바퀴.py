import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def calc_score(wheel_list):
    score = 0
    if wheel_list[0][0] == 1:
        score += 1
    if wheel_list[1][0] == 1:
        score += 2
    if wheel_list[2][0] == 1:
        score += 4
    if wheel_list[3][0] == 1:
        score += 8
    return score


# def left(wheel_list, i, direction):
#     if i < 0:
#         return
#     if wheel_list[i][2] != wheel_list[i+1][2]:


# def right(wheel_list, i, direction):
#     if 3 < i:
#         return


def f(wheel_list, rotation):
    i, r = rotation
    i -= 1

    rotation_tmp = []
    nt = r
    for j in range(i - 1, -1, -1):
        if wheel_list[j][2] != wheel_list[j + 1][6]:
            nt *= -1
            rotation_tmp.append((j, nt))
        else:
            break
    nt = r
    for j in range(i + 1, 4):
        if wheel_list[j][6] != wheel_list[j - 1][2]:
            nt *= -1
            rotation_tmp.append((j, nt))
        else:
            break

    for rotation in rotation_tmp:
        wheel_list[rotation[0]].rotate(rotation[1])

    wheel_list[i].rotate(r)


def solution():
    wheel_list = [deque(list(map(int, input()))) for _ in range(4)]
    n = int(input())
    rotations = [list(map(int, input().split())) for _ in range(n)]

    for rotation in rotations:
        f(wheel_list, rotation)
    print(calc_score(wheel_list))


solution()
