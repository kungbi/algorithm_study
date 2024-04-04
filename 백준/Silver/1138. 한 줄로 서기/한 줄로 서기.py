import sys
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    for comb in permutations(range(n), n):
        result = True
        for i in range(n):
            count = 0
            for j in range(i):
                if comb[i] < comb[j]:
                    count += 1
            if count != arr[comb[i]]:
                result = False
                break
        if result:
            print(*list(map(lambda x: x + 1, comb)))
            break


solution()
