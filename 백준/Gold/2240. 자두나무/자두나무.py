import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    T, W = map(int, input().split())
    arr = [0] + [int(input()) for _ in range(T)]
    # 움직이거나 안움직이거나
    # 각 초에 대한 움직인 위치에 따른 자두를 먹은 횟수
    # dp[i][j] i초에 j번 움직인 경우 먹은 자두의 수

    dp = [[0] * (W + 1) for _ in range((T + 1))]
    for i in range(1, T + 1):
        for j in range(min(i + 1, W + 1)):
            tmp = None
            if j % 2 == 0:
                tmp = 1
            else:
                tmp = 2

            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1 if j != 0 else 0])
            if arr[i] == tmp:
                dp[i][j] += 1
    print(max(dp[-1]))


main()
