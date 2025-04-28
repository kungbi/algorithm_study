import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    prefix_sum = [0]
    for i in range(n):
        if arr[i] == 1:
            prefix_sum.append(prefix_sum[i] + 1)
        else:
            prefix_sum.append(prefix_sum[i] - 1)
    print(abs(max(prefix_sum) - min(prefix_sum)))


main()
