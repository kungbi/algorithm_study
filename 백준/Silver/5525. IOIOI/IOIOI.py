import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    m = int(input())
    arr = list(input())

    dp = [0]
    if arr[0] == 'I' and arr[1] == 'O' and arr[2] == 'I':
        dp[0] = 1
    else:
        dp[0] = 0

    i = 1
    while i < m - 2:
        if arr[i] == 'I' and arr[i + 1] == 'O' and arr[i + 2] == 'I':
            dp.append(dp[-1] + 1)
            i += 1
        else:
            dp.append(0)
        i += 1

    result = 0
    for num in dp:
        if n <= num:
            result += 1
    print(result)

solution()