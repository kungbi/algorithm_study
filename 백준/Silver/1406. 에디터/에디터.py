import sys


def input():
    return sys.stdin.readline().rstrip()


def P_command(A, B, c):
    A.append(c)


def L_command(A, B):
    if A:
        B.append(A.pop())


def D_command(A, B):
    if B:
        A.append(B.pop())


def B_command(A):
    if A:
        A.pop()


def solution():
    A = list(input())
    B = []
    m = int(input())

    for _ in range(m):
        tmp = input().split()
        if tmp[0] == "P":
            c = tmp[1]
            P_command(A, B, c)
            continue

        if tmp[0] == "L":
            L_command(A, B)
        elif tmp[0] == "D":
            D_command(A, B)
        elif tmp[0] == "B":
            B_command(A)

    B.reverse()
    print("".join(A) + "".join(B))


solution()

