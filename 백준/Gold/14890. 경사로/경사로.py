import sys


def input():
    return sys.stdin.readline().rstrip()


def is_available(arr):
    global n

    visited = [False] * n
    num = arr[0]
    i = 1
    while i < n:
        if arr[i] < num - 1 or num + 1 < arr[i]:
            return False
        elif num - 1 == arr[i]:
            num -= 1
            for j in range(l):
                if not i + j < n:
                    return False
                if visited[i + j] == True:
                    return False
                if arr[i + j] != num:
                    return False
                visited[i + j] = True
        elif num == arr[i] - 1:
            for j in range(1, l + 1):
                if not 0 <= i - j:
                    return False
                if visited[i - j] == True:
                    return False
                if arr[i - j] != num:
                    return False
                visited[i - j] = True
            num += 1
        i += 1
    return True


def solution():
    global n, l

    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        if is_available(arr[i]):
            answer += 1
        if is_available([arr[j][i] for j in range(n)]):
            answer += 1
    print(answer)


solution()
