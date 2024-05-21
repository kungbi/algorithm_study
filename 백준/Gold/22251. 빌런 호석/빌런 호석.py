import sys


def input():
    return sys.stdin.readline().rstrip()


def f(index, x, cost, p):
    global answer

    if len(x) <= index:
        answer.append(int("".join(map(str, x))))
        return

    origin_num = x[index]
    for i in range(10):
        n_cost = switch_info[origin_num][i]
        if n_cost <= p:
            x[index] = i
            f(index + 1, x, cost + n_cost, p - n_cost)
            x[index] = origin_num


switch_info = segment_info = None
answer = []


def solution():
    global switch_info, segment_info, answer

    n, k, p, x = map(int, input().split())
    switch_info = [[0] * 10 for _ in range(10)]
    segment_info = [119, 36, 93, 109, 46, 107, 123, 37, 127, 111]

    x_list = list(map(int, list(str(x))))
    if len(x_list) < k:
        x_list = [0] * (k - len(x_list)) + x_list

    for i in range(10):
        for j in range(10):
            switch_info[i][j] = bin(segment_info[i] ^ segment_info[j]).count("1")

    f(0, x_list, 0, p)
    answer = set(filter(lambda a: a != x and 1 <= a <= n, answer))
    print(len(answer))


solution()
