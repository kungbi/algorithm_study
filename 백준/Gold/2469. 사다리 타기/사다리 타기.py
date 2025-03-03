import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    k = int(input())
    n = int(input())
    expect = list(input())

    arr = [list(input()) for _ in range(n)]
    left = 0
    right = n - 1

    arr_left = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:k]
    arr_right = expect

    while left < right:
        if not "?" in arr[left]:
            for i in range(k - 1):
                if arr[left][i] == "-":
                    arr_left[i], arr_left[i + 1] = arr_left[i + 1], arr_left[i]
            left += 1
        if not "?" in arr[right]:
            for i in range(k - 1):
                if arr[right][i] == "-":
                    arr_right[i], arr_right[i + 1] = arr_right[i + 1], arr_right[i]
            right -= 1

    result = ""
    for i in range(k - 1):
        if arr_left[i] == arr_right[i + 1] and arr_left[i + 1] == arr_right[i]:
            result += "-"
        else:
            result += "*"
    for i in range(k - 1):
        if result[i] == "-":
            arr_left[i], arr_left[i + 1] = arr_left[i + 1], arr_left[i]
    if arr_left != arr_right:
        return "x" * (k - 1)

    return result


print(main())
