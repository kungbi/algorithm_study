import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    arr = [int(input()) for _ in range(m)]

    dp = [(a, b, 0)]
    for idx, num in enumerate(arr):
        tmp = []
        for a, b, c in dp:
            if a == num or b == num:
                tmp.append((a, b, c))
                continue
            tmp.append((num, b, c + abs(num - a)))
            tmp.append((a, num, c + abs(num - b)))
        dp = tmp
    print(min(dp, key=lambda x: x[2])[2])


main()
