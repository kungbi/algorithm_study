import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y, w, s = map(int, input().split())

    answer = float("inf")
    answer = min(answer, (x + y) * w)
    answer = min(answer, min(x, y) * s + abs(x - y) * w)
    if (x + y) % 2 == 0:
        answer = min(answer, max(x, y) * s)
    if (x + y) % 2 == 1:
        answer = min(answer, max(x, y) * s + w)
        answer = min(answer, (max(x, y) - 1) * s + w)
    print(answer)


main()
