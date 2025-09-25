import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            prefix_sum[y][x] = (
                prefix_sum[y - 1][x]
                + prefix_sum[y][x - 1]
                + arr[y][x]
                - prefix_sum[y - 1][x - 1]
            )

    for _ in range(m):
        y1, x1, y2, x2 = map(int, input().split())
        tmp = (
            prefix_sum[y2][x1 - 1] + prefix_sum[y1 - 1][x2] - prefix_sum[y1 - 1][x1 - 1]
        )
        print(prefix_sum[y2][x2] - tmp)


main()
