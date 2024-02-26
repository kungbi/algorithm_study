def solution(arr):
    n = len(arr)
    
    min_val = 0
    max_val = 0
    sum_val = 0
    
    i = n - 1
    while 0 <= i:
        if arr[i] == '-':
            num = int(arr[i + 1])
            tmp_max_val = max_val
            tmp_min_val = min_val
            
            # min값 갱신
            # - (a + b), -a + b
            min_val = min(-(sum_val + tmp_max_val), -(sum_val) + tmp_min_val)
            
            # max값 갱신
            # - (a + b), -a + b
            mid_val = sum_val - num
            max_val = max(-(sum_val + tmp_min_val), - num + (mid_val + tmp_max_val))
            sum_val = 0
        elif arr[i] != '+':
            sum_val += int(arr[i])
        i -= 1
    return sum_val + max_val