import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.reverse()

        result = 0
        max_v = 0
        for num in arr:
            if max_v < num:
                max_v = num
            else:
                result += max_v - num
        print(result)


solution()
