import sys
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]

    bags.sort()
    jewels.sort(key=lambda x: x[0])

    heap = []
    answer = 0
    for bag in bags:
        while jewels and jewels[0][0] <= bag:
            heappush(heap, -jewels[0][1])
            heappop(jewels)

        if heap:
            answer += -heappop(heap)
    print(answer)


main()
