import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a_arr = []
    b_arr = []
    c_arr = []
    d_arr = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        a_arr.append(a)
        b_arr.append(b)
        c_arr.append(c)
        d_arr.append(d)

    AB_combinations = []
    CD_combinations = []
    for i in range(n):  # n
        for j in range(n):  # n
            AB_combinations.append(a_arr[i] + b_arr[j])
            CD_combinations.append(c_arr[i] + d_arr[j])

    CD_counter = Counter(CD_combinations)

    answer = 0
    for num in AB_combinations:
        answer += CD_counter[-num]
    print(answer)


main()
