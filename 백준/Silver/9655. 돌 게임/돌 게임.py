import sys


def input():
    return sys.stdin.readline().rstrip()


def switch(a):
    return (a + 1) % 2


def main():
    n = int(input())
    dp = [-1] * (n + 1)
    dp[0] = 1

    for i in range(1, n):
        if 0 <= i - 1:
            dp[i] = switch(dp[i - 1])
        if 0 <= i - 3:
            dp[i] = switch(dp[i - 3])
    print("SK" if dp[n - 1] == 1 else "CY")


main()
