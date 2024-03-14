import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr1 = []
        arr2 = []
        for _ in range(n):
            a, b = map(int, input().split())
            arr1.append((a, b))
            arr2.append((a, b))
        arr1.sort(key=lambda x: x[0])
        arr2.sort(key=lambda x: x[1])
        # print(arr1)
        # print(arr2)

        deleted = []
        min1 = float("inf")
        min2 = float("inf")
        for i in range(1, n):
            min1 = min(min1, arr1[i - 1][1])
            if min1 < arr1[i][1]:
                deleted.append(arr1[i])
            min2 = min(min2, arr2[i - 1][0])
            if min2 < arr2[i][0]:
                deleted.append(arr2[i])

        result = set(arr1) - set(deleted)
        # print(set(deleted))
        print(len(result))


solution()
