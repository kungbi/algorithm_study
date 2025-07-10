import sys
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    heap = []
    for _ in range(n):
        for num in tuple(map(int, input().split())):
            if n < len(heap):
                heappop(heap)
            heappush(heap, num)
    if n < len(heap):
        heappop(heap)
    print(heappop(heap))


main()
