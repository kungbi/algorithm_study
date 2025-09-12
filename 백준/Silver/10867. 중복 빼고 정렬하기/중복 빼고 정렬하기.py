import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*sorted(set(arr)))


main()
