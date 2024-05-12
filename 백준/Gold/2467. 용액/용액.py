import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    min_num = sys.maxsize
    answer = []
    for i in range(n - 1):
        left = i + 1
        right = n - 1
        num = arr[i]
        while left <= right:
            mid = (left + right) // 2
            mid_num = arr[mid]

            # print(num, mid_num)
            if abs(num + mid_num) < min_num:
                min_num = abs(num + mid_num)
                answer = [num, mid_num]

            if mid_num < -num:
                left = mid + 1
            else:
                right = mid - 1
    print(*answer)


solution()
