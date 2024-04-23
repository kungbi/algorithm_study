import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    arr = list(input())
    n = len(arr)
    arr *= 2

    k = 0
    for c in arr[:n]:
        if c == "a":
            k += 1

    result = float("inf")
    for i in range(n):
        count = 0
        for j in range(i, i + k):
            if arr[j] == "b":
                count += 1
        result = min(result, count)
    print(result)


solution()
