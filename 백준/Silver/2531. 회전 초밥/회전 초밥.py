import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, d, k, c = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    counter = defaultdict(int)
    kind = 0
    for i in range(k):
        arr.append(arr[i])
        if counter[arr[i]] == 0:
            kind += 1
        counter[arr[i]] += 1

    result = 0
    for i in range(n):
        result = max(result, kind if counter[c] != 0 else kind + 1)

        counter[arr[i]] -= 1
        if counter[arr[i]] == 0:
            kind -= 1
        if counter[arr[i + k]] == 0:
            kind += 1
        counter[arr[i + k]] += 1

    print(result)


solution()
