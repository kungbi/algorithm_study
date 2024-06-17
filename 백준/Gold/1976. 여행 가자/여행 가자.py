import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    m = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    plan = list(map(int, input().split()))
    for i in range(m):
        plan[i] -= 1

    visited = [False] * n
    visited[plan[0]] = True
    queue = deque([plan[0]])
    while queue:
        curr = queue.popleft()
        for j in range(n):
            if arr[curr][j] == 1 and visited[j] == False:
                visited[j] = True
                queue.append(j)

    for num in set(plan):
        if visited[num] == False:
            print("NO")
            return
    print("YES")


solution()
