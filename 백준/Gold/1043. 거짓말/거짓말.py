import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    aware_set = set()
    if tmp[0]:
        aware_set = set(tmp[1:])
    party_sets = [set(list(map(int, input().split()))[1:]) for _ in range(m)]

    for _ in range(m):
        aware_party_count = 0
        for i in range(m):
            if aware_set & party_sets[i]:
                aware_set = aware_set.union(party_sets[i])
                aware_party_count += 1
    print(m - aware_party_count)


solution()
