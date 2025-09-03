import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())

    sets = set()
    for _ in range(n):
        sets.add(input())

    for _ in range(m):
        for c in input().split(","):
            if c not in sets:
                continue
            sets.remove(c)
        print(len(sets))


main()
