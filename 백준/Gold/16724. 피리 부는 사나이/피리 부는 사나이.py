import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def convert2dir(x):
    if x == "U":
        return 0
    if x == "D":
        return 1
    if x == "L":
        return 2
    if x == "R":
        return 3


dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]


def is_frame(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def join(disjoint_set, a, b):
    a_parent = find(disjoint_set, a)
    b_parent = find(disjoint_set, b)

    if a_parent != b_parent:
        x, y = b_parent
        disjoint_set[y][x] = a_parent


def find(disjoint_set, pos):
    x, y = pos
    if disjoint_set[y][x] == pos:
        return disjoint_set[y][x]
    disjoint_set[y][x] = find(disjoint_set, disjoint_set[y][x])
    return disjoint_set[y][x]


def main():
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    disjoint_set = [[(x, y) for x in range(m)] for y in range(n)]
    for y in range(n):
        for x in range(m):
            dir = convert2dir(arr[y][x])

            a = (x, y)
            b = (x + dxs[dir], y + dys[dir])
            if find(disjoint_set, a) != find(disjoint_set, b):
                join(disjoint_set, a, b)

    answer_set = set()
    for y in range(n):
        for x in range(m):
            answer_set.add(find(disjoint_set, (x, y)))
    print(len(answer_set))


main()
