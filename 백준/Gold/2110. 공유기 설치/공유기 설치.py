import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    left = 0
    right = arr[-1] - arr[0]
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        count = 1
        curr = arr[0]
        for i in range(1, n):
            if curr + mid <= arr[i]:
                curr = arr[i]
                count += 1

        if c <= count:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    print(answer)


solution()
