import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    input()

    dp = [0] * (n + 1)

    prefix_sum = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = prefix_sum + 1
        if i < k:
            prefix_sum += dp[i]

    # print(dp)
    print(dp[k] * math.comb(n, k) % 1_000_000_007)


main()
