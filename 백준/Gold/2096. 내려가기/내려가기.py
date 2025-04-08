import sys
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    prev_max = deepcopy(arr[0])
    prev_min = deepcopy(arr[0])

    curr_max = [0] * 3
    curr_min = [0] * 3

    for i in range(1, n):
        curr_max[0] = max(prev_max[0], prev_max[1]) + arr[i][0]
        curr_max[1] = max(prev_max) + arr[i][1]
        curr_max[2] = max(prev_max[1], prev_max[2]) + arr[i][2]

        curr_min[0] = min(prev_min[0], prev_min[1]) + arr[i][0]
        curr_min[1] = min(prev_min) + arr[i][1]
        curr_min[2] = min(prev_min[1], prev_min[2]) + arr[i][2]

        prev_max = deepcopy(curr_max)
        prev_min = deepcopy(curr_min)

    print(max(prev_max), min(prev_min))


main()
