import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    # 배열에 존재하는 숫자를 빠르게 확인하기 위해 set 사용
    num_set = set(arr)

    # 점수 저장
    score = defaultdict(int)

    # 최대 숫자
    max_num = max(arr)

    # 배수 관계를 활용하여 점수 계산
    for num in arr:
        for multiple in range(num * 2, max_num + 1, num):
            if multiple in num_set:
                score[num] += 1
                score[multiple] -= 1

    # 결과 출력
    print(" ".join(str(score[num]) for num in arr))


main()
