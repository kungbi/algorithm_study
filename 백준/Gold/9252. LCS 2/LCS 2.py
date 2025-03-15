import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def f(dp, X, Y, x, y):
    if x == 0 or y == 0:
        return ""

    tmp = X[x - 1] if X[x - 1] == Y[y - 1] else ""

    if X[x - 1] == Y[y - 1]:
        return f(dp, X, Y, x - 1, y - 1) + X[x - 1]
    elif dp[y - 1][x] <= dp[y][x - 1]:
        return f(dp, X, Y, x - 1, y)

    return f(dp, X, Y, x, y - 1)


def main():
    X = list(input())
    Y = list(input())

    dp = [[0] * (len(X) + 1) for _ in range(len(Y) + 1)]
    for i in range(1, len(Y) + 1):
        for j in range(1, len(X) + 1):
            if Y[i - 1] == X[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[len(Y)][len(X)]
    print(lcs_length)
    if lcs_length != 0:
        print(f(dp, X, Y, len(X), len(Y)))


main()
