import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def multi(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]

    for row in range(n):
        for column in range(n):
            for i in range(n):
                result[row][column] += A[row][i] * B[i][column]
            result[row][column] %= 1_000
    return result


def solution(matrix, m):
    if m == 1:
        return [[x % 1000 for x in row] for row in matrix]

    tmp = solution(matrix, m // 2)
    if m % 2 == 0:
        return multi(tmp, tmp)
    return multi(multi(tmp, tmp), matrix)


def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = solution(matrix, m)

    for row in answer:
        print(*row)


main()

