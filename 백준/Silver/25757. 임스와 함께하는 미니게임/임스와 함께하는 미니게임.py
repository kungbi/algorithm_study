import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, game = input().split()
    n = int(n)
    arr = set([input() for _ in range(n)])

    if game == "Y":
        return len(arr)
    if game == "F":
        return len(arr) // 2
    if game == "O":
        return len(arr) // 3


print(main())
