import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y):
    return 0 <= x < 3 and 0 <= y < 3


def is_sorted(arr):
    for i in range(1, 8):
        prev_v = arr[i - 1]
        curr_v = arr[i]
        if prev_v > curr_v:
            return False
    return True


def arr2str(arr):
    return "".join(["".join(list(map(str, row))) for row in arr])


def swap_str(string, a, b):
    string_copy = list(string)

    x, y = a
    a_i = y * 3 + x
    x, y = b
    b_i = y * 3 + x

    string_copy[a_i], string_copy[b_i] = string_copy[b_i], string_copy[a_i]
    return "".join(string_copy)


def f(arr, pos):
    global result

    dict = defaultdict(str)
    queue = deque([(arr2str(arr), pos, 0)])
    while queue:
        curr_str, pos, d = queue.popleft()
        x, y = pos

        if x == 2 and y == 2 and is_sorted(curr_str):
            result = min(result, d)
            continue

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if not is_frame(nx, ny):
                continue

            next_str = swap_str(curr_str, pos, (nx, ny))
            if not dict[next_str]:
                dict[next_str] = d + 1
                queue.append((next_str, (nx, ny), d + 1))


result = float("inf")


def solution():
    global result

    arr = [list(map(int, input().split())) for _ in range(3)]
    pos = None
    for y in range(3):
        for x in range(3):
            if arr[y][x] == 0:
                pos = (x, y)

    f(arr, pos)
    if result == float("inf"):
        result = -1
    print(result)


solution()
