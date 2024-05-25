import sys


def input():
    return sys.stdin.readline().rstrip()


def f(arr, string, index):
    global answer

    if len(arr) <= index:
        answer.append(string)
        return

    for c in " -+":
        f(arr, string + c + str(arr[index]), index + 1)


def parse(equation):
    global pos

    num = 0
    while pos < len(equation) and equation[pos] not in "-+":
        num *= 10
        num += int(equation[pos])
        pos += 1
    return num


def calc(equation):
    global pos

    pos = 0
    equation = equation.replace(" ", "")
    start = parse(equation)

    while pos < len(equation):
        if equation[pos] == "-":
            pos += 1
            start -= parse(equation)
        elif equation[pos] == "+":
            pos += 1
            start += parse(equation)
    return start


answer = []
pos = 0


def solution():
    global answer

    t = int(input())
    for _ in range(t):
        answer = []
        n = int(input())
        f(list(range(1, n + 1)), "1", 1)
        answer.sort()
        for ans in answer:
            if calc(ans) == 0:
                print(ans)
        print()


solution()
