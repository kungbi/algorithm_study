import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    h, w = map(int, input().split())
    height_list = list(map(int, input().split()))

    arr = [[0] * w for _ in range(h)]
    for i in range(w):
        for j in range(height_list[i]):
            arr[j][i] = 1

    count = 0
    for i in range(h):
        start = -1
        end = -1
        j = 0
        while (start == -1 or end == -1) and j < w:
            if arr[i][j] == 1:
                if start == -1:
                    start = j
                elif end == -1:
                    end = j
            if start != -1 and end != -1:
                count += end - start - 1
                start = end
                end = -1
            j += 1
    print(count)


solution()
