import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(m):
    a, b = 1, 1

    for i in range(m**2):
        a, b = b, (a + b) % m

        if a == 1 and b == 1:
            return i + 1


def main():
    p = int(input())

    for _ in range(p):
        n, m = map(int, input().split())
        answer = solution(m)
        print(n, answer)


main()
