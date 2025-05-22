import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def combinations(arr, num, idx):
    if len(arr) <= idx:
        return [num]
    tmp = []
    tmp += combinations(arr, num + arr[idx], idx + 1)
    tmp += combinations(arr, num, idx + 1)
    return tmp


def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    left_arr = arr[: n // 2]
    right_arr = arr[n // 2 :]

    left_elements = combinations(left_arr, 0, 0)
    right_elements = sorted(combinations(right_arr, 0, 0))

    answer = 0
    for num in left_elements:
        left_idx = bisect.bisect_left(right_elements, s - num)
        right_idx = bisect.bisect_right(right_elements, s - num)

        answer += right_idx - left_idx

    if s == 0:
        answer -= 1
    print(answer)


main()
