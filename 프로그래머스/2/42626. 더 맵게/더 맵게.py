from heapq import heappush
from heapq import heappop
from heapq import heapify

def solution(scoville, K):
    heap = []
    for num in scoville:
        heappush(heap, num)
    
    answer = 0
    while heap:
        if len(heap) < 2:
            break
            
        if K <= heap[0]:
            break
            
        a, b = heappop(heap), heappop(heap) 
        heappush(heap, a + b * 2)
        answer += 1
        
    return answer if K <= heap[0] else -1
    