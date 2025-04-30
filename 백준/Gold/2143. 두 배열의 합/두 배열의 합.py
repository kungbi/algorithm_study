import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    prefix_sum_A = [0]
    prefix_sum_B = [0]
    for i in range(n):
        prefix_sum_A.append(prefix_sum_A[i] + A[i])
    for i in range(m):
        prefix_sum_B.append(prefix_sum_B[i] + B[i])

    A_sum = defaultdict(int)
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            A_sum[prefix_sum_A[j] - prefix_sum_A[i]] += 1
    B_sum = defaultdict(int)
    for i in range(m + 1):
        for j in range(i + 1, m + 1):
            B_sum[prefix_sum_B[j] - prefix_sum_B[i]] += 1

    answer = 0
    for num in A_sum.keys():
        if T - num in B_sum:
            answer += A_sum[num] * B_sum[T - num]
    print(answer)


main()
