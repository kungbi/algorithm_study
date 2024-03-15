import sys
from heapq import heappop
from heapq import heappush
from heapq import heapify


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    heapify(arr)

    for _ in range(m):
        a = heappop(arr)
        b = heappop(arr)
        heappush(arr, a + b)
        heappush(arr, a + b)

    print(sum(arr))


solution()
