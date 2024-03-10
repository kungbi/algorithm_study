import sys


def input():
    return sys.stdin.readline().rstrip()


def is_possible(arr, x, y):
    for col in range(x):
        if arr[col] == y:
            return False
        if abs(arr[col] - y) == abs(col - x):
            return False
    return True


def f(arr, visited, x):
    if x == n:
        return 1

    cnt = 0
    for y in range(n):
        if visited[y] == False:
            if is_possible(arr, x, y):
                visited[y] = True
                arr[x] = y
                cnt += f(arr, visited, x + 1)
                visited[y] = False

    return cnt


n = 0


def solution():
    global n

    n = int(input())
    arr = [-1] * n
    visited = [False] * n
    result = f(arr, visited, 0)
    print(result)


solution()
