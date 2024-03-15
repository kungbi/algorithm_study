import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    dist = list(map(int, input().split()))
    price = list(map(int, input().split()))

    min_price = float("inf")

    money = 0
    i = 0
    while i < n - 1:
        min_price = min(min_price, price[i])
        money += dist[i] * min_price
        i += 1
    print(money)


solution()
