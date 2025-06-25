import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    dp = [1, 2]
    for _ in range(300_000):
        dp.append((dp[-1] * 2) % 1_000_000_007)

    arr = list(map(int, input().split()))
    arr.sort()

    answer = 0
    for i in range(n - 1):
        answer -= (arr[i] * (dp[n - 1 - i] - 1)) % 1_000_000_007
    for i in range(n - 1, 0, -1):
        answer += (arr[i] * (dp[i] - 1)) % 1_000_000_007

    print(answer % 1_000_000_007)


main()
