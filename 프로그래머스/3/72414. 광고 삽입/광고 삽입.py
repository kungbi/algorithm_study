def time2sec(time):
    h, m, s = map(int, time.split(':'))
    sec = h * 3600 + m * 60 + s
    return sec
    

def solution(play_time, adv_time, logs):
    arr = [0] * (time2sec(play_time) + 2)
    
    for log in logs:
        start, end = log.split('-')
        start_i = time2sec(start)
        end_i = time2sec(end)
        arr[start_i] += 1
        arr[end_i] -= 1
    
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]
        
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]
    
    max_v = 0
    max_t = 0            
    adv_s = time2sec(adv_time)
    for i in range(adv_s - 1, len(arr)):
        tmp = arr[i] - arr[i - adv_s]
        if i < adv_s:
            tmp = arr[i]
        if max_v < tmp:
            max_v = tmp
            max_t = i - adv_s + 1

    h = max_t // (60 * 60)
    m = (max_t % (60 * 60)) // 60
    s = (max_t % (60 * 60)) % 60
    return(str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2))
    
    