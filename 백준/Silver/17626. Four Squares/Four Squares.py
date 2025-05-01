import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    dp = [0] * (n + 1)

    k = 1
    while k**2 <= n:
        dp[k**2] = 1
        k += 1

    for i in range(1, n + 1):
        if dp[i] != 0:
            continue

        if dp[i] == 0:
            dp[i] = dp[1] + dp[i - 1]
        j = 1
        while j**2 <= i:
            dp[i] = min(dp[i], dp[j**2] + dp[i - j**2])
            j += 1

    print(dp[n])


main()
