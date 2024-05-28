def is_one(num):
    while num // 5:
        if num % 5 == 2:
            return False
        num //= 5
    
    return False if num % 5 == 2 else True

def solution(n, l, r):
    answer = 0
    for i in range(l - 1, r):
        answer += 1 if is_one(i) else 0
    return answer
        