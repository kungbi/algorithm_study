from itertools import combinations


def solution():
    arr = []
    for _ in range(9):
        num = int(input())
        arr.append(num)

    for case in combinations(arr, 7):
        if sum(case) == 100:
            for num in sorted(case):
                print(num)
            break


solution()
