import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    m = int(input())
    arr = input()

    i = 0
    dp = 0
    result = 0
    while i < m - 2:
        if arr[i:i + 3] == "IOI":
            dp += 1
            i += 1
        else:
            dp = 0
        if n <= dp:
            result += 1
        i += 1
    print(result)

solution()