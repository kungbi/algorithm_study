import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    sum_num = float("inf")
    sum_numbers = None
    for fixed in range(n):
        left = 0
        right = n - 1
        target = -1 * arr[fixed]
        while left < right:
            if left == fixed:
                left += 1
                continue
            if right == fixed:
                right -= 1
                continue

            a = arr[left]
            b = arr[right]
            sum_ab = a + b
            if abs(target - sum_ab) < sum_num:
                sum_num = abs(target - sum_ab)
                sum_numbers = (arr[fixed], a, b)

            if target < sum_ab:
                right -= 1
            elif sum_ab < target:
                left += 1
            elif target == sum_ab:
                break

    print(*sorted(sum_numbers))


main()
