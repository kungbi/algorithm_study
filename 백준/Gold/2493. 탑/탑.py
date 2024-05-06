import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n

    for i in range(1, n):
        if arr[i - 1] >= arr[i]:
            dp[i] = i
        else:
            j = i - 1
            while 0 < dp[j] and arr[dp[j] - 1] < arr[i]:
                if j == 0 or dp[j] == 0:
                    break
                j = dp[j] - 1
            dp[i] = dp[j]
    print(*dp[: n + 1])


solution()
