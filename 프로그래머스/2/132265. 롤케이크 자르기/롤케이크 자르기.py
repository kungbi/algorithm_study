from collections import Counter


def solution(topping):
    a_count = Counter(topping[:1])
    b_count = Counter(topping[1:])
    a = 1
    b = len(b_count)
    
    answer = 0
    for i in range(1, len(topping)):
        a_count[topping[i]] += 1
        if a_count[topping[i]] == 1:
            a += 1
            
        b_count[topping[i]] -= 1
        if b_count[topping[i]] == 0:
            b -= 1
        
        if a == b:
            answer += 1
    return answer
        
        