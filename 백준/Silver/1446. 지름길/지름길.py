import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, d = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, input().split())))
    arr.sort(key=lambda x: x[0])
    arr = deque(arr)

    dp = [float("inf")] * (10_001)
    dp[0] = 0
    i = 0
    while i <= d:
        if 0 < i:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        while arr and arr[0][0] == i:
            s, e, cost = arr.popleft()
            dp[e] = min(dp[e], dp[i] + cost)
        i += 1
    print(dp[d])


solution()
