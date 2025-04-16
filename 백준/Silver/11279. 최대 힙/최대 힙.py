import sys
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    heap = []
    for _ in range(n):
        num = int(input())
        if num != 0:
            heappush(heap, -num)
        else:
            if not heap:
                print(0)
                continue
            print(-heap[0])
            heappop(heap)


main()
