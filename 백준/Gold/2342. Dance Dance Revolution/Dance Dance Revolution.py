import sys


def input():
    return sys.stdin.readline().rstrip()


def diff(a, b):
    if a == b:
        return 1
    if a == 0 or b == 0:
        return 2
    if abs(a - b) == 2:
        return 4
    return 3


def main():
    arr = list(map(int, input().split()))
    arr.pop()
    n = len(arr)
    INF = float("inf")
    dp = [[[INF] * 5 for _ in range(5)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(n):
        for l in range(5):
            for r in range(5):
                if dp[i][l][r] == INF:
                    continue

                if arr[i] != r:
                    dp[i + 1][arr[i]][r] = min(
                        dp[i + 1][arr[i]][r], dp[i][l][r] + diff(l, arr[i])
                    )
                if arr[i] != l:
                    dp[i + 1][l][arr[i]] = min(
                        dp[i + 1][l][arr[i]], dp[i][l][r] + diff(r, arr[i])
                    )

    answer = INF
    for l in range(5):
        for r in range(5):
            answer = min(answer, dp[n][l][r])
    print(answer)


main()
