import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(a, b, c):
    if b == 1:
        return a % c

    muli_num = solution(a, b // 2, c)
    if b % 2 == 0:
        return (muli_num**2) % c
    return (muli_num**2 * a) % c


def main():
    a, b, c = map(int, input().split())

    print(solution(a, b, c))


main()
