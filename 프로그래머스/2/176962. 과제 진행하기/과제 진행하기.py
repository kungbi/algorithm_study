from collections import deque

def solution(plans):
    plans.sort(key=lambda x: x[1])
    
    tmp_queue = deque()
    main_queue = deque()
    for plan in plans:
        time = list(map(int, plan[1].split(':')))
        main_queue.append([plan[0], time[0]*60 + time[1], int(plan[2])])
    
    answer = []
    time = 0
    task = None
    while main_queue or tmp_queue:
        if main_queue:
            if main_queue[0][1] == time:
                tmp_queue.appendleft(task)
                task = main_queue.popleft()
        if not task and tmp_queue:
            task = tmp_queue.popleft()
        
        if task:
            task[2] -= 1
            if task[2] == 0:
                answer.append(task[0])
                task = None
        time += 1
            
    return answer