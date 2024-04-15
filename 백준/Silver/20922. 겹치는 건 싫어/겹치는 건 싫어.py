import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 0
    counter = defaultdict(int)
    left = 0
    right = 0
    while left < n and right < n:
        if counter[arr[right]] < k:
            counter[arr[right]] += 1
            right += 1
        elif counter[arr[right]] == k:
            if left <= right:
                counter[arr[left]] -= 1
                left += 1

        answer = max(answer, right - left)
    print(answer)


solution()
