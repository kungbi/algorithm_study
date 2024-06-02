import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = float("inf")
    sum_num = 0
    left = 0
    right = 0
    while True:
        if s <= sum_num:
            answer = min(answer, right - left)
            sum_num -= arr[left]
            left += 1
        elif right == n:
            break
        else:
            sum_num += arr[right]
            right += 1

    print(answer if answer != float("inf") else 0)


solution()
