import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    children = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        children[x].append(y)
        children[y].append(x)

    queue = deque([(a, 0)])
    visited = [False] * (n + 1)
    visited[a] = True
    while queue:
        curr, cost = queue.popleft()
        if curr == b:
            return cost
        for child in children[curr]:
            if visited[child]:
                continue
            queue.append((child, cost + 1))
            visited[child] = True


tmp = main()
print(tmp if tmp else -1)
