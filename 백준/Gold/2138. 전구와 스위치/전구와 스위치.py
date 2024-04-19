import sys
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


def push(arr, i):
    arr[i] ^= 1
    if 0 < i:
        arr[i - 1] ^= 1
    if i < len(arr) - 1:
        arr[i + 1] ^= 1


def solution():
    n = int(input())
    src = list(map(int, input()))
    dest = list(map(int, input()))

    answer_list = []

    # 0을 안 눌렀을 때
    count = 0
    arr = deepcopy(src)
    for i in range(1, n):
        if arr[i - 1] != dest[i - 1]:
            count += 1
            push(arr, i)
    if dest == arr:
        answer_list.append(count)

    # 0을 눌렀을 때
    arr = deepcopy(src)
    count = 1
    push(arr, 0)
    for i in range(1, n):
        if arr[i - 1] != dest[i - 1]:
            count += 1
            push(arr, i)
    if dest == arr:
        answer_list.append(count)

    print(min(answer_list) if answer_list else -1)


solution()
