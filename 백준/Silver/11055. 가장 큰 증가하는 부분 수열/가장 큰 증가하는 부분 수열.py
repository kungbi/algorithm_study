import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [0] * n
    for i, num in enumerate(arr):
        dp[i] = num

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    print(max(dp))


main()
