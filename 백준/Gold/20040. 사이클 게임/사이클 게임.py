import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def union(parents, a, b):
    a_root = find(parents, a)
    b_root = find(parents, b)

    if a_root != b_root:
        parents[b_root] = a_root


def find(parents, node):
    if node == parents[node]:
        return node
    parents[node] = find(parents, parents[node])
    return parents[node]


def main():
    n, m = map(int, input().split())
    parents = [i for i in range(n)]
    arr = [tuple(map(int, input().split())) for _ in range(m)]

    answer = 0
    for round, (a, b) in enumerate(arr, start=1):
        if find(parents, a) == find(parents, b):
            answer = round
            break

        union(parents, a, b)

    return answer


print(main())
