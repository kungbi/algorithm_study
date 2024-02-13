import sys
def input():
    return sys.stdin.readline().rstrip()

def calc_length(arr, height):
    result = 0
    for num in arr:
        tmp = num - height
        if 0 < tmp:
            result += tmp
    return result

def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    start = 0
    end = 1_000_000_000

    result = 0
    while start <= end:
        mid = (start + end) // 2
        length = calc_length(arr, mid)
        if m <= length:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)

solution()