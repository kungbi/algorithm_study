import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = [[0] * 1001 for _ in range(1001)]

    max_h = 0
    max_l = 0
    for _ in range(n):
        l, h = map(int, input().split())
        if max_h < h:
            max_l = l
            max_h = h
        for j in range(h + 1):
            arr[j][l] = 1

    result = max_h  # 가장 긴 기둥의 넓이
    left_i = max_l - 1
    right_i = max_l + 1

    # print()
    for h in range(max_h, -1, -1):
        left_i_tmp = 0
        right_i_tmp = 1000

        # left_i에서 왼쪽으로 탐색
        while left_i_tmp <= left_i and arr[h][left_i_tmp] != 1:
            left_i_tmp += 1

        # right_i에서 오른쪽으로 탐색
        while right_i <= right_i_tmp and arr[h][right_i_tmp] != 1:
            right_i_tmp -= 1

        # print(left_i_tmp, right_i_tmp)

        # 만약 발견하면 해당 높이에서 발견한 위치의 곱을 더하기
        if left_i_tmp <= left_i:
            width = abs(left_i - left_i_tmp) + 1
            result += width * h
            left_i = left_i_tmp - 1
        if right_i <= right_i_tmp:
            width = abs(right_i - right_i_tmp) + 1
            result += width * h
            right_i = right_i_tmp + 1

    print(result)


solution()
