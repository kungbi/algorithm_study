from re import L
import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    dp = [1, 1]
    a = b = 1
    for _ in range(n**2):
        tmp = (a + b) % 1_000_000
        a, b = b, tmp
        if a == 1 and b == 1:
            dp.pop()
            break
        dp.append(b)

    print(dp[(n - 1) % len(dp)])


main()
