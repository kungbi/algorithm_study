import sys


def input():
    return sys.stdin.readline().rstrip()


def max_solution(n):
    result = ""
    if 3 <= n and n % 2 == 1:
        result = "7"
        n -= 3

    result += "1" * (n // 2)
    return result


def main():
    match_sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [0, 0, 1, 7, 4, 2, 6, 8]
    for i in range(8, 101):
        dp.append(float("inf"))
        for j in range(len(match_sticks)):
            if i - match_sticks[j] < 2:
                continue
            dp[-1] = min(dp[i], dp[i - match_sticks[j]] * 10 + j)

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp[n], max_solution(n))


main()
