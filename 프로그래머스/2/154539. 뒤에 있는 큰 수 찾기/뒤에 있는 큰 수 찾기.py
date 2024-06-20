from heapq import heappush
from heapq import heappop

def solution(numbers):
    result = [0] * len(numbers)
    heap = []
    for i in range(len(numbers) - 1, -1, -1):
        if heap:
            while heap and numbers[i] >= heap[0]:
                num = heappop(heap)
            if heap and numbers[i] < heap[0]:
                result[i] = heap[0]
            else:
                result[i] = -1
        else:
            result[i] = -1
        heappush(heap, numbers[i])
    return result
    