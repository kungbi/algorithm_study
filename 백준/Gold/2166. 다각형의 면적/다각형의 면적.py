import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(arr):
    n = len(arr)

    answer = 0
    for i in range(n - 1):
        a = arr[i]
        b = arr[i + 1]

        answer += a[0] * b[1] - a[1] * b[0]
    return abs(answer) / 2


def main():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.append(arr[0])

    answer = solution(arr)
    print(round(answer, 1))


main()
