import sys
from collections import defaultdict
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())

    in_degree = [0] * (n + 1)
    next_number = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        next_number[a].append(b)
        in_degree[b] += 1

    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heappush(heap, i)

    answer = []
    while heap:
        idx = heappop(heap)
        answer.append(idx)
        for n_idx in next_number[idx]:
            in_degree[n_idx] -= 1
            if in_degree[n_idx] == 0:
                heappush(heap, n_idx)
    print(*answer)


main()
