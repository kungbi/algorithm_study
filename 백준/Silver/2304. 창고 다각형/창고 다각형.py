import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    columns = defaultdict(int)

    max_l = 0
    max_h = 0
    for _ in range(n):
        l, h = map(int, input().split())
        columns[l] = h
        if max_h < h:
            max_h = h
            max_l = l
    result = max_h

    num = 0
    for x in range(1, max_l):
        if num < columns[x]:
            num = columns[x]
        result += num

    num = 0
    for x in range(1000, max_l, -1):
        if num < columns[x]:
            num = columns[x]
        result += num
    print(result)


solution()
