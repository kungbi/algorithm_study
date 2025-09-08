import sys


def input():
    return sys.stdin.readline().rstrip()


answer = 0


def solution(arr, idx, n, dp):
    global answer

    if idx == n:
        return 1
    if dp[idx][arr[idx - 1]] != -1:
        return dp[idx][arr[idx - 1]]

    tmp = 0
    if arr[idx - 1] == 0:
        arr[idx] = 1
        tmp += solution(arr, idx + 1, n, dp)

    arr[idx] = 0
    tmp += solution(arr, idx + 1, n, dp)

    dp[idx][arr[idx - 1]] = tmp
    return tmp


def main():
    n = int(input())
    arr = [0] * n
    dp = [[-1, -1] for _ in range(n)]

    arr[0] = 1
    answer = solution(arr, 1, n, dp)
    print(answer)


"""
n은 90이 최대

4 -> 1000, 1001, 1010

1
10
-> 101 -> 1010
-> 100 -> 1001
       -> 1000



"""


main()
