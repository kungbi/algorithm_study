import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def is_door(c):
    return ord("A") <= ord(c) <= ord("Z")


def is_key(c):
    return ord("a") <= ord(c) <= ord("z")


def find_start_points(arr):
    h, w = len(arr), len(arr[0])

    result = []
    for x in range(w):
        if arr[0][x] != "*" and not is_door(arr[0][x]):
            result.append((x, 0))
        if arr[h - 1][x] != "*" and not is_door(arr[h - 1][x]):
            result.append((x, h - 1))
    for y in range(h):
        if y == 0 or y == h - 1:
            continue
        if arr[y][0] != "*" and not is_door(arr[y][0]):
            result.append((0, y))
        if arr[y][w - 1] != "*" and not is_door(arr[y][w - 1]):
            result.append((w - 1, y))
    return result


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_frame(x, y, w, h):
    return 0 <= x < w and 0 <= y < h


def find_doors(arr, start_points):
    h, w = len(arr), len(arr[0])

    queue = deque(start_points)
    visited = [[False] * w for _ in range(h)]
    for x, y in start_points:
        visited[y][x] = True
    result = []

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not is_frame(nx, ny, w, h):
                continue
            if visited[ny][nx]:
                continue
            if is_door(arr[ny][nx]):
                visited[ny][nx] = True
                result.append((nx, ny))
                continue
            if arr[ny][nx] != "*":
                visited[ny][nx] = True
                queue.append((nx, ny))
    return result


def find_keys_n_collect(arr, start_points, keys):
    global answer

    h, w = len(arr), len(arr[0])
    queue = deque(start_points)

    visited = [[False] * w for _ in range(h)]
    for x, y in start_points:
        visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        if is_key(arr[y][x]):
            keys[arr[y][x]] = True
            arr[y][x] = "."
        if arr[y][x] == "$":
            answer += 1
            arr[y][x] = "."

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not is_frame(nx, ny, w, h):
                continue
            if visited[ny][nx]:
                continue
            if arr[ny][nx] != "*" and not is_door(arr[ny][nx]):
                visited[ny][nx] = True
                queue.append((nx, ny))
                continue


def solution(arr, keys):
    start_points = find_start_points(arr)

    stop = False
    while not stop:
        start_points = find_start_points(arr)
        find_keys_n_collect(arr, start_points, keys)
        doors = find_doors(arr, start_points)

        stop = True
        for door in doors:
            x, y = door

            if arr[y][x].lower() not in keys:
                continue

            if arr[y][x] == ".":
                continue
            arr[y][x] = "."
            stop = False


answer = 0


def main():
    global answer

    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        arr = []
        arr.append("." * (w + 2))
        for _ in range(h):
            arr.append(["."] + list(input()) + ["."])
        arr.append("." * (w + 2))

        key = input()

        keys = defaultdict(bool)
        if key != "0":
            for c in key:
                keys[c] = True

        answer = 0
        solution(arr, keys)
        print(answer)


main()
