import sys
from collections import deque
from heapq import heappush
from heapq import heappop

MAX_SIZE = 100_000


def input():
    return sys.stdin.readline().rstrip()


def is_frame(x):
    return 0 <= x <= MAX_SIZE


def bfs(n, k):
    queue = deque([n])
    dp = [float("inf")] * (MAX_SIZE + 1)
    dp[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            return dp[x]

        for dx, dc in [(-1, 1), (1, 1), (x, 0)]:
            nx = x + dx
            nc = dp[x] + dc
            if is_frame(nx) and nc < dp[nx]:
                dp[nx] = nc
                queue.append(nx)


def solution():
    n, k = map(int, input().split())
    print(bfs(n, k))


solution()
