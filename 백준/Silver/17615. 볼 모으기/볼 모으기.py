import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = input()

    answer_list = []

    answer_list.append(arr.lstrip("R").count("R"))
    answer_list.append(arr.rstrip("R").count("R"))

    answer_list.append(arr.lstrip("B").count("B"))
    answer_list.append(arr.rstrip("B").count("B"))

    print(min(answer_list))


solution()
