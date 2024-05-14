import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = [0] + [int(input()) for _ in range(n)]
    answer = []

    for i in range(1, n + 1):
        select = i
        visited = [False] * (n + 1)
        while visited[select] == False:
            visited[select] = True
            select = arr[select]
        if select == i:
            answer.append(i)

    answer.sort()
    print(len(answer))
    for num in answer:
        print(num)


solution()
