import sys


def input():
    return sys.stdin.readline().rstrip()


def get_sum(coins):
    result = 0
    for coin, count in coins:
        result += coin * count
    return result


def solution(coins):
    total = get_sum(coins)
    if total % 2 == 1:
        return 0

    dp = [False] * (total // 2 + 1)
    dp[0] = True
    for coin, count in coins:
        for i in range(total // 2, -1, -1):
            if i - coin < 0:
                continue
            if dp[i - coin] == False:
                continue

            for j in range(count):
                if len(dp) <= i + coin * j:
                    continue
                dp[i + coin * j] = True

    if dp[total // 2]:
        return 1
    return 0


def main():

    for _ in range(3):
        n = int(input())
        coins = [tuple(map(int, input().split())) for _ in range(n)]
        coins.sort(reverse=True)

        print(solution(coins))


main()
