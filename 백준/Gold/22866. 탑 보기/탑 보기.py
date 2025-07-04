import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    buildings = list(map(int, input().split()))
    answers = [[0, float("inf")] for _ in range(n)]

    stack = []
    for i in range(n):
        hight = buildings[i]
        while stack and stack[-1][0] <= hight:
            stack.pop()

        answers[i][0] += len(stack)
        if stack and abs(stack[-1][1] - i) < abs(answers[i][1] - i):
            answers[i][1] = stack[-1][1]
        if stack and abs(stack[-1][1] - i) == abs(answers[i][1] - i):
            answers[i][1] = min(answers[i][1], stack[-1][1])
        stack.append((hight, i))

    stack = []
    for i in range(n - 1, -1, -1):
        hight = buildings[i]
        while stack and stack[-1][0] <= hight:
            stack.pop()

        answers[i][0] += len(stack)
        if stack and abs(stack[-1][1] - i) < abs(answers[i][1] - i):
            answers[i][1] = stack[-1][1]
        if stack and abs(stack[-1][1] - i) == abs(answers[i][1] - i):
            answers[i][1] = min(answers[i][1], stack[-1][1])
        stack.append((hight, i))

    for answer in answers:
        if answer[0] != 0:
            print(answer[0], answer[1] + 1)
        else:
            print(0)


main()
