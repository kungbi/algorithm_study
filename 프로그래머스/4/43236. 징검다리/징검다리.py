def solution(distance, rocks, n):
    rocks.sort()
    start = 1
    end = distance
    
    rocks.append(distance)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        x = 0
        
        delete_cnt = 0
        for rock in rocks:
            if rock - x < mid:
                delete_cnt += 1
            else:
                x = rock
        
        if n < delete_cnt:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer