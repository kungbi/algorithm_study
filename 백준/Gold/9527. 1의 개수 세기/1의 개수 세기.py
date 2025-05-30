import sys


def input():
    return sys.stdin.readline().rstrip()


def count_bit(num):
    result = 0
    while num:
        num = num & (num - 1)
        result += 1
    return result


def solution(dp, num):
    binary = bin(num)[2:]
    n = len(binary)
    result = 0
    for i in range(n):
        if binary[i] == "0":
            continue
        level = n - i - 1
        result += 1
        result += dp[level]
        result += num - 2**level
        num -= 2**level

    return result


def main():
    a, b = map(int, input().split())

    dp = [0, 1]

    i = 1
    curr = 1
    while curr * 2 <= b:
        dp.append(dp[i] * 2 + 2**i)
        curr *= 2
        i += 1

    print(solution(dp, b) - solution(dp, a - 1))


main()
