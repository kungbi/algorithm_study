import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution():
    F, S, G, U, D = map(int, input().split())

    queue = deque([(S, 0)])
    visited = [False] * (F + 1)
    visited[S] = True

    while queue:
        stair, count = queue.popleft()

        if stair == G:
            print(count)
            return

        for num in [U, -D]:
            next_stair = stair + num
            if 1 <= next_stair <= F and visited[next_stair] == False:
                visited[next_stair] = True
                queue.append((next_stair, count + 1))

    print("use the stairs")


solution()
