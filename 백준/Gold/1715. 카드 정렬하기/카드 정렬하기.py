import sys
from heapq import heappop
from heapq import heappush
from heapq import heapify


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    heapify(arr)
    result = 0
    while 2 <= len(arr):
        a = heappop(arr)
        b = heappop(arr)
        result += a + b
        heappush(arr, a + b)

    print(result)


solution()
