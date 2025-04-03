import sys
from bisect import bisect_right


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    A = list(map(int, input().split()))

    lis = []
    for num in A:
        if not lis:
            lis.append(num)
        elif lis[-1] < num:
            lis.append(num)
        else:
            idx = bisect_right(lis, num)
            if lis[idx - 1] != num:
                lis[idx] = num

    return len(lis)


print(main())
