import sys
from collections import defaultdict
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


def f(coin_list, total):
    total //= 2
    dp = [True] + [False] * total
    for C, N in coin_list:
        for i in range(total, C - 1, -1):
            if not dp[i - C]:
                continue

            for j in range(N + 1):
                if i + C * j <= total:
                    dp[i + C * j] = True
        if dp[-1]:
            return 1
    return 0


def solution():
    for _ in range(3):
        n = int(input())
        coin_list = []
        total = 0
        for _ in range(n):
            coin, cnt = map(int, input().split())
            coin_list.append((coin, cnt))
            total += coin * cnt
        if total % 2 != 0:
            print(0)
        else:
            print(f(coin_list, total))


solution()
