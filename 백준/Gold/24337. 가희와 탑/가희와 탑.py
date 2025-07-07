import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())
    answer = []
    for i in range(1, a):
        answer.append(i)
    answer.append(max(a, b))
    for i in range(b - 1, 0, -1):
        answer.append(i)

    if n < len(answer):
        print(-1)
        return
    if a == 1:
        answer = [answer[0]] + [1] * (n - len(answer)) + answer[1:]
        print(*answer)
        return

    answer = [1] * (n - len(answer)) + answer
    print(*answer)


main()
