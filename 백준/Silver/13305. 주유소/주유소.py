import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    dist = [0] + list(map(int, input().split()))
    price = list(map(int, input().split()))

    money = 0
    for i in range(n - 1):
        next_dist = dist[i + 1]
        if i != 0:
            if price[i - 1] * next_dist < price[i] * next_dist:
                money += price[i - 1] * next_dist
            else:
                money += next_dist * price[i]
        else:
            money += next_dist * price[i]

    print(money)


solution()
