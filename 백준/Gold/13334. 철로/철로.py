from heapq import heappop, heappush
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    d = int(input())

    filtered_arr = []
    for h, o in arr:
        if d < abs(h - o):
            continue
        filtered_arr.append(sorted([h, o]))

    filtered_arr.sort(key=lambda x: x[1])

    start_heap = []
    answer = 0
    count = 0
    for line in filtered_arr:
        a, b = line

        heappush(start_heap, a)
        count += 1

        while start_heap and start_heap[0] < b - d:
            count -= 1
            heappop(start_heap)
        answer = max(answer, count)
    print(answer)


main()
