import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())  # 최대 5,000
    arr = list(map(int, input().split()))  # 10,000개, 요소 <= 100,000
    arr.sort()

    answer = float("inf")
    for i in range(n):
        answer = min(answer, arr[i] + arr[-i - 1])
    print(answer)


main()
