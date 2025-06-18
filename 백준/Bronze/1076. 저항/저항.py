import sys


def input():
    return sys.stdin.readline().rstrip()


nums = [
    [0, 1],
    [1, 10],
    [2, 100],
    [3, 1_000],
    [4, 10_000],
    [5, 100_000],
    [6, 1_000_000],
    [7, 10_000_000],
    [8, 100_000_000],
    [9, 1_000_000_000],
]


def get_id(color):
    if color == "black":
        return 0
    if color == "brown":
        return 1
    if color == "red":
        return 2
    if color == "orange":
        return 3
    if color == "yellow":
        return 4
    if color == "green":
        return 5
    if color == "blue":
        return 6
    if color == "violet":
        return 7
    if color == "grey":
        return 8
    if color == "white":
        return 9


def main():
    arr = [input() for _ in range(3)]

    result = ""
    result += str(nums[get_id(arr[0])][0])
    result += str(nums[get_id(arr[1])][0])
    print(int(result) * nums[get_id(arr[2])][1])


main()
