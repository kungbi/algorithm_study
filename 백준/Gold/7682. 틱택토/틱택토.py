import sys


def input():
    return sys.stdin.readline().rstrip()


def count(arr):
    o_count = 0
    x_count = 0
    for i in range(9):
        if arr[i] == "X":
            x_count += 1
        if arr[i] == "O":
            o_count += 1

    return o_count, x_count


def is_win(arr, char):
    count = 0
    if arr[0] == arr[1] == arr[2] == char:
        count += 1
    if arr[3] == arr[4] == arr[5] == char:
        count += 1
    if arr[6] == arr[7] == arr[8] == char:
        count += 1

    if arr[0] == arr[3] == arr[6] == char:
        count += 1
    if arr[1] == arr[4] == arr[7] == char:
        count += 1
    if arr[2] == arr[5] == arr[8] == char:
        count += 1

    if arr[0] == arr[4] == arr[8] == char:
        count += 1
    if arr[2] == arr[4] == arr[6] == char:
        count += 1
    return count


def solution(arr):
    o_count, x_count = count(arr)
    o_win = is_win(arr, "O")
    x_win = is_win(arr, "X")

    if o_win and x_win == 0 and o_count == x_count:
        return "valid"
    if x_win and o_win == 0 and x_count - 1 == o_count:
        return "valid"
    if x_win == 0 and o_win == 0 and x_count == 5 and o_count == 4:
        return "valid"

    return "invalid"


def main():
    while True:
        arr = input()
        if arr == "end":
            return

        print(solution(arr))


main()
