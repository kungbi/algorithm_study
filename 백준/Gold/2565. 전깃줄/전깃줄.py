import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()

    arr2 = []
    for i in range(n):
        arr2.append(arr[i][1])

    dp = [1] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr2[j] < arr2[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(n - max(dp))


main()
