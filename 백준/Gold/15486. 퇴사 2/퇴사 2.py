import sys
from heapq import heappush
from heapq import heappop
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    work_list = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)
    answer = 0
    heap = []
    prev_max = 0

    for i in range(n):
        end_idx = i + work_list[i][0] - 1

        if n <= end_idx:
            continue

        while heap and heap[0][0] < i:
            prev_max = max(prev_max, heap[0][1])
            heappop(heap)

        dp[end_idx] = max(dp[end_idx], prev_max + work_list[i][1])
        heappush(heap, (end_idx, dp[end_idx]))

        answer = max(answer, dp[end_idx])

    print(answer)


solution()
