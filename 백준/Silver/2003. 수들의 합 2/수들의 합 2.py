import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split())) + [0]

    l = r = 0
    num = 0
    answer = 0
    while l <= n and r <= n:
        if num < m:
            num += arr[l]
            l += 1
        else:
            num -= arr[r]
            r += 1

        if num == m:
            answer += 1
    print(answer)


main()
