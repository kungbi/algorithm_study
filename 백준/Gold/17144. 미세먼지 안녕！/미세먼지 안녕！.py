from inspect import isframe
import sys


def input():
    return sys.stdin.readline().rstrip()


def get_air_purifier_pos(arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x][0] == -1:
                return (x, y), (x, y + 1)


dxs = [0, -1, 1, 0]
dys = [-1, 0, 0, 1]


def is_frame(x, y, r, c):
    return 0 <= x < c and 0 <= y < r


def spread_dust(arr, x, y, r, c):
    spreaded_count = 0
    std_dust_amount = arr[y][x][0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not is_frame(nx, ny, r, c):
            continue
        if arr[ny][nx][0] == -1:
            continue

        spreaded_count += 1
        arr[ny][nx][1] += std_dust_amount // 5
    arr[y][x][1] -= std_dust_amount // 5 * spreaded_count


def update_dust(arr, r, c):
    for y in range(r):
        for x in range(c):
            arr[y][x][0] += arr[y][x][1]
            arr[y][x][1] = 0


def process_dust(arr, r, c):
    for y in range(r):
        for x in range(c):
            if 0 < arr[y][x][0]:
                spread_dust(arr, x, y, r, c)
    update_dust(arr, r, c)


def roate_dir(dx, dy, dir):
    dx, dy = dy, dx
    if dir == 0:
        dy *= -1
    if dir == 1:
        dx *= -1
    return dx, dy


# dir: 0 -> 왼쪽, 1 -> 오른쪽
def process_air_purifier(arr, r, c, air_purifier, dir):
    x, y = air_purifier
    dx = 1
    dy = 0

    nx = x + dx
    ny = y + dy
    prev = [0, 0]
    while nx != air_purifier[0] or ny != air_purifier[1]:
        if not is_frame(nx, ny, r, c):
            dx, dy = roate_dir(dx, dy, dir)
            nx, ny = x + dx, y + dy
            continue

        x, y = nx, ny
        arr[y][x], prev = prev, arr[y][x]
        nx, ny = x + dx, y + dy


def main():
    r, c, t = map(int, input().split())
    arr = []
    for _ in range(r):
        tmp = []
        for num in map(int, input().split()):
            tmp.append([num, 0])
        arr.append(tmp)

    air_purifier1, air_purifier2 = get_air_purifier_pos(arr)

    for _ in range(t):
        process_dust(arr, r, c)
        process_air_purifier(arr, r, c, air_purifier1, 0)
        process_air_purifier(arr, r, c, air_purifier2, 1)

    answer = 0
    for y in range(r):
        for x in range(c):
            answer += arr[y][x][0]
    print(answer + 2)


main()
