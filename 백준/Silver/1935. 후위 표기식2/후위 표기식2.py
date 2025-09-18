import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def is_operator(c):
    if c == "-":
        return True
    elif c == "+":
        return True
    elif c == "/":
        return True
    elif c == "*":
        return True
    return False


def operate(a, b, operation):
    if operation == "-":
        return a - b
    elif operation == "+":
        return a + b
    elif operation == "/":
        return a / b
    elif operation == "*":
        return a * b


def main():
    N = int(input())
    inputs = deque(list(input()))

    values = dict()
    for c in range(ord("A"), ord("A") + N):
        values[chr(c)] = int(input())

    stack = []
    while inputs:
        tmp = inputs.popleft()
        if is_operator(tmp):
            b, a = stack.pop(), stack.pop()
            value = operate(a, b, tmp)
            stack.append(value)
        else:
            stack.append(values[tmp])
    print(format(stack[-1], ".2f"))


main()
