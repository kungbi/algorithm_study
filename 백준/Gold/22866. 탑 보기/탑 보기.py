import sys
from heapq import heappush
from heapq import heappop


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    buildings = list(map(int, input().split()))
    answers = [[0, -1] for _ in range(n)]

    heap = []
    for idx, hight in enumerate(buildings):
        while heap and heap[0][0] <= hight:
            heappop(heap)
        answers[idx][0] += len(heap)

        if heap and answers[idx][1] == -1:
            answers[idx][1] = heap[0]
        elif heap:
            if abs(idx - heap[0][1]) < abs(idx - answers[idx][1][1]):
                answers[idx][1] = heap[0]

        heappush(heap, (hight, idx))

    heap = []
    for idx in range(n - 1, -1, -1):
        hight = buildings[idx]
        while heap and heap[0][0] <= hight:
            heappop(heap)
        answers[idx][0] += len(heap)

        if heap and answers[idx][1] == -1:
            answers[idx][1] = heap[0]
        elif heap:
            if abs(idx - heap[0][1]) < abs(idx - answers[idx][1][1]):
                answers[idx][1] = heap[0]

        heappush(heap, (hight, idx))

    for answer in answers:
        if answer[0]:
            print(answer[0], answer[1][1] + 1)
        else:
            print(0)


main()
