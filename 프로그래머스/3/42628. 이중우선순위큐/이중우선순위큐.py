from heapq import heappush
from heapq import heappop

def solution(operations):
    maxheap = []
    minheap = []

    for operation in operations:
        oper, n = operation.split()
        n = int(n)
        
        if oper == 'I':
            heappush(maxheap, -n)
            heappush(minheap, n)
        elif oper == 'D' and maxheap and minheap:
            if n == 1: # pop max
                heappop(maxheap)
                if not maxheap or -maxheap[0] < minheap[0]:
                    maxheap = []
                    minheap = []
            elif n == -1: # pop min
                heappop(minheap)
                if not minheap or minheap[0] > -maxheap[0]:
                    maxheap = []
                    minheap = []
                
    if maxheap and minheap:
        return(-maxheap[0], minheap[0])
    return ([0, 0])