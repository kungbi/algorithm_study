import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = " " + input()
    b = " " + input()

    dp = [[0] * (len(b)) for _ in range(len(a))]
    result = 0
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
    print(result)


main()
