import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    t = int(input())

    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if x1 == x2 and y1 == y2:
            if r1 == r2:
                print(-1)
                continue
            print(0)
            continue
        if r1 + r2 == distance or abs(r1 - r2) == distance:
            print(1)
            continue
        if r1 + r2 < distance or distance < abs(r1 - r2):
            print(0)
            continue
        print(2)


main()
