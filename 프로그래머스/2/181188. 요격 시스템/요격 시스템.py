from heapq import heappush
from heapq import heappop

def solution(targets):
    targets.sort(key=lambda x: x[1])
    
    count = 0
    shot_x = -1
    for target in targets:
        s, e = target
        if s < shot_x <= e:
            continue
        
        shot_x = e
        count += 1
    return count
                
        