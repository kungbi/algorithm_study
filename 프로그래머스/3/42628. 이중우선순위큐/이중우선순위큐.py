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
            if n == 1:
                num = -heappop(maxheap)
                if num in minheap:
                    minheap.remove(num)
            elif n == -1:
                num = heappop(minheap)
                if num in maxheap:
                    maxheap.remove(num)
    if maxheap and minheap:
        return(-maxheap[0], minheap[0])
    return ([0, 0])