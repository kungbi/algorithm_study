import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())  # <= 1,000
    arr = list(map(int, input().split()))  # 0 <= x <= 10,000

    # 연속적인 그룹을 나누어서 최대, 최소값의 차이 들의 최대 합
    # 1000개임. O(N^2)까지 가능할듯?
    dp = [0] * (n + 1)
    for i in range(0, n):
        low = 10_000
        high = 0
        for j in range(i + 1):
            low = min(low, arr[i - j])
            high = max(high, arr[i - j])

            tmp = abs(low - high)
            dp[i] = max(dp[i], dp[i - j - 1] + tmp)
    print(dp[n - 1])


main()
