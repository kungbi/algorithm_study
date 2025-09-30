import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    string = input()
    if string == string[::-1]:
        return 1
    return 0


print(main())
