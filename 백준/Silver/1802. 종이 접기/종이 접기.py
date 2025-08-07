import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        for i in range(mid):
            if arr[i] == arr[right - i]:
                return "NO"
        right = mid - 1
    return "YES"


def main():
    t = int(input())
    for _ in range(t):
        arr = input()
        print(solution(arr))


main()
