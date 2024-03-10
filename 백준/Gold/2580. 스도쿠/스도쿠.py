import sys


def input():
    return sys.stdin.readline().rstrip()


def get_candidate(arr, pos):
    visited = [0] * 10
    x, y = pos
    for i in range(9):
        a = arr[y][i]
        b = arr[i][x]
        visited[a] += 1
        visited[b] += 1

    tx = x // 3 * 3
    ty = y // 3 * 3

    for y in range(ty, ty + 3):
        for x in range(tx, tx + 3):
            a = arr[y][x]
            visited[a] += 1

    result = []
    for i in range(1, 10):
        if visited[i] == 0:
            result.append(i)
    return result


def f(arr, blank_list, i):
    if i == len(blank_list):
        for row in arr:
            print(*row)
        exit()

    candidate_list = get_candidate(arr, blank_list[i])
    for candidate in candidate_list:
        x, y = blank_list[i]
        arr[y][x] = candidate
        f(arr, blank_list, i + 1)
        arr[y][x] = 0

    return -1


def solution():
    arr = [list(map(int, input().split())) for _ in range(9)]
    blank_list = []

    for y in range(9):
        for x in range(9):
            if arr[y][x] == 0:
                blank_list.append((x, y))

    f(arr, blank_list, 0)


solution()
