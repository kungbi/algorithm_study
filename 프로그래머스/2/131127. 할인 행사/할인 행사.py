def solution(want, number, discount):
    n = len(discount)
    m = len(number)
    want_index = {}
    for i in range(len(want)):
        want_index[want[i]] = i
        
    answer = 0
    sol = 0
    left = right = 0
    while left < n and right < n:
        if sol != m:
            if discount[right] in want_index:
                number[want_index[discount[right]]] -= 1
                if number[want_index[discount[right]]] == 0:
                    sol += 1
            right += 1
        else:
            if discount[left] in want_index:
                number[want_index[discount[left]]] += 1
                if number[want_index[discount[left]]] == 1:
                    sol -= 1
            left += 1
        
        if sol == m and right - left <= 10:
            answer += 1
            
    return answer