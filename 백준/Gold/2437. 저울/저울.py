import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    dp = [0, 0]
    for i in range(n):
        next_dp = [dp[0] + arr[i], dp[1] + arr[i]]
        if dp[1] + 1 < next_dp[0]:
            return dp[1] + 1
        dp[1] = next_dp[1]
    return dp[1] + 1


print(solution())
