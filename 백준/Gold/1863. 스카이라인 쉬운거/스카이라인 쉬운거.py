import sys
from heapq import heappop
from heapq import heappush


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    pos_list = []
    for _ in range(n):
        pos_list.append(tuple(map(int, input().split())))

    answer = 0
    heap = []
    for _, y in pos_list:
        if heap and -heap[0] < y:
            heappush(heap, -y)
        else:
            while heap and y < -heap[0]:
                heappop(heap)
                answer += 1
            if (heap and -heap[0] != y) or not heap:
                heappush(heap, -y)

    answer += sum(1 for num in heap if 0 < -num)
    print(answer)


solution()
