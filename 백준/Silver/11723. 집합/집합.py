import sys
def input():
    return sys.stdin.readline().rstrip()


def solution():
    m = int(input())
    result = set()
    for _ in range(m):
        command = input().split()
        num = None
        if len(command) == 2:
            num = int(command[1])
            command = command[0]
        else:
            command = command[0]

        if command == "add":
            result = result | set([num])
        elif command == "check":
            if num in result:
                print(1)
            else:
                print(0)
        elif command == "remove":
            result = result - set([num])
        elif command == "toggle":
            if num in result:
                result = result - set([num])
            else:
                result = result | set([num])
        elif command == "all":
            result = set(list(range(1, 21)))
        elif command == "empty":
            result = set()

solution()