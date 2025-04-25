import sys
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    arr = tuple(map(int, input().split()))
    results = list(permutations(arr, m))
    results.sort()
    for row in results:
        for num in row:
            print(num, end=" ")
        print()


main()
