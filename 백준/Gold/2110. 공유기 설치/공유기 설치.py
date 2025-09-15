import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    low = 1
    high = arr[-1] - arr[0]
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        count = 1
        last = arr[0]

        for pos in arr[1:]:
            if mid <= pos - last:
                count += 1
                last = pos

        if c <= count:
            answer = mid
            low = mid + 1  # 더 크게 가능?
        else:
            high = mid - 1

    print(answer)


main()
