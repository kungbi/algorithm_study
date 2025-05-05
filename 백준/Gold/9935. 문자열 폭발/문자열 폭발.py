import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    arr = input()
    explosion = input()

    stack = []
    for char in arr:
        stack.append(char)

        if len(stack) < len(explosion):
            continue
        a_str = "".join(stack[-(len(explosion)) : :])
        if a_str == explosion:
            for _ in range(len(explosion)):
                stack.pop()
    answer = "".join(stack)
    print(answer if answer != "" else "FRULA")


main()
