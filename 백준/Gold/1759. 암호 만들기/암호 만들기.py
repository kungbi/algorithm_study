import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


def check(arr):
    a = 0
    b = 0
    for c in arr:
        if c in "aeiou":
            a += 1
        else:
            b += 1
    if 1 <= a and 2 <= b:
        return True
    return False


def solution():
    l, c = map(int, input().split())
    arr = input().split()
    arr.sort()
    for result in combinations(arr, l):
        if check(result):
            print("".join(result))


solution()
