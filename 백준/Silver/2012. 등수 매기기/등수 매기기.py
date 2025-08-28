import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    answer = 0
    for i in range(n):
        answer += abs(arr[i] - (i + 1))
    print(answer)


main()
