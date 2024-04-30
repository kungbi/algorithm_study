import sys


def input():
    return sys.stdin.readline().rstrip()


def belt_rotate(belt):
    for i in range(len(belt) - 1, 0, -1):
        if belt[i - 1] == True:
            belt[i] = True
            belt[i - 1] = False


def rotate(durability):
    return [durability[-1]] + durability[:-1]


def solution():
    n, k = map(int, input().split())
    durability = list(map(int, input().split()))
    belt = [False] * n

    broken = 0
    time = 0
    while broken < k:
        time += 1

        # belt 회전
        durability = rotate(durability)
        belt_rotate(belt)
        if belt[-1] == True:
            belt[-1] = False

        # 로봇 이동
        for i in range(n - 2, 0, -1):
            if belt[i] == True and belt[i + 1] == False and 0 < durability[i + 1]:
                durability[i + 1] -= 1
                if durability[i + 1] == 0:
                    broken += 1
                belt[i] = False
                belt[i + 1] = True
        if belt[-1] == True:
            belt[-1] = False

        # 로봇 올리기
        if durability[0] != 0:
            belt[0] = True
            durability[0] -= 1
            if durability[0] == 0:
                broken += 1

    print(time)


solution()
