import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0
    now_arr = []
    for i in range(k):
        if arr[i] in now_arr:
            continue

        if len(now_arr) != n:
            now_arr.append(arr[i])
        else:
            # 제일 늦게 나오는 것
            tmp_set = set(now_arr)

            for j in range(i + 1, k):
                if len(tmp_set) == 1:
                    break
                tmp_set = tmp_set - set([arr[j]])

            min_x = 0
            tmp_list = list(tmp_set)
            if tmp_list:
                min_x = tmp_list[0]

            now_arr.remove(min_x)
            result += 1
            now_arr.append(arr[i])
    print(result)


solution()
