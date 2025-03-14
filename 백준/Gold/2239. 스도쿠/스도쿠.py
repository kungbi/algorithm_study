import sys
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


result = None


def get_available_numbers(arr, x, y):
    numbers = set([i for i in range(1, 10)])
    for i in range(9):
        numbers -= set([arr[y][i]])
        numbers -= set([arr[i][x]])
    for i in range(3):
        xx = x - (x % 3)
        yy = y - (y % 3)
        numbers -= set([arr[yy][xx + i]])
        numbers -= set([arr[yy + 1][xx + i]])
        numbers -= set([arr[yy + 2][xx + i]])
    return numbers


def solution(arr, x, y):
    global result

    if x == 9:
        x = 0
        y += 1
    if y == 9:
        result = deepcopy(arr)
        return True

    if arr[y][x] != 0:
        return solution(arr, x + 1, y)

    available_numbers = get_available_numbers(arr, x, y)
    if not available_numbers:
        return False
    for num in tuple(available_numbers):
        arr[y][x] = num
        if solution(arr, x + 1, y):
            return True
        arr[y][x] = 0

    return False


def main():
    arr = [list(map(int, input())) for _ in range(9)]
    solution(arr, 0, 0)

    for row in result:
        print("".join(map(str, row)))


main()
