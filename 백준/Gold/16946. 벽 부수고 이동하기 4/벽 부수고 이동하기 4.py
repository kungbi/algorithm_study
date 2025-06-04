import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]


def is_frame(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def one_to_minus(arr, n, m):
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                arr[y][x] = -1


def bfs(arr, pos, i):
    n = len(arr)
    m = len(arr[0])
    x, y = pos

    queue = deque([(x, y)])
    arr[y][x] = i
    count = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not is_frame(nx, ny, n, m):
                continue
            if arr[ny][nx] != 0:
                continue

            queue.append((nx, ny))
            arr[ny][nx] = i
            count += 1
    return count


def main():
    n, m = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    one_to_minus(arr, n, m)

    i = 1
    counter = defaultdict(int)
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 0:
                counter[i] = bfs(arr, (x, y), i)
                i += 1

    answer = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if arr[y][x] != -1:
                continue

            i_set = set()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not is_frame(nx, ny, n, m):
                    continue
                if arr[ny][nx] == -1:
                    continue
                i_set.add(arr[ny][nx])
            num = 1
            for i in i_set:
                num += counter[i]
            answer[y][x] = num % 10

    for row in answer:
        print("".join(map(str, row)))


main()
