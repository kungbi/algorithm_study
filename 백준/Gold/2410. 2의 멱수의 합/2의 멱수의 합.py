import sys


def input():
    return sys.stdin.readline().rstrip()


def is_power(n):
    while 1 < n:
        if n % 2 == 1:
            return False
        n //= 2
    return True


def main():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1

    i = 1
    while i <= n:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
            dp[j] %= 1_000_000_000
        i *= 2
    # print(dp)
    print(dp[n])


main()
