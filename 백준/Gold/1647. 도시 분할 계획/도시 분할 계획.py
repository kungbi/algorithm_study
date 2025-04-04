import sys


def input():
    return sys.stdin.readline().rstrip()


class DisjointSet:
    def __init__(self, n):
        self.arr = [i for i in range(n)]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if root_a != root_b:
            self.arr[root_b] = root_a

    def find(self, x):
        if self.arr[x] != x:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]


def main():
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    edges.sort(key=lambda x: x[2])

    disjoint_set = DisjointSet(n + 1)
    costs = []
    for edge in edges:
        a, b, c = edge

        if disjoint_set.find(a) != disjoint_set.find(b):
            disjoint_set.union(a, b)
            costs.append(c)

    return sum(costs) - max(costs)


print(main())
