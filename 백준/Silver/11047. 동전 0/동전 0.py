import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.reverse()

    result = 0
    for i in range(n):
        tmp = k // arr[i]
        if 0 < tmp:
            result += tmp
            k %= arr[i]
    print(result)


solution()
