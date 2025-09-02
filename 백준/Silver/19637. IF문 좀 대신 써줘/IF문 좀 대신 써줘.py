import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    rank_names = []
    rank_limits = []
    for _ in range(n):
        a, b = input().split()
        b = int(b)
        rank_names.append(a)
        rank_limits.append(b)

    for _ in range(m):
        num = int(input())
        idx = bisect.bisect_left(rank_limits, num)
        if len(rank_names) <= idx:
            print(rank_names[-1])
        else:
            print(rank_names[idx])


main()
