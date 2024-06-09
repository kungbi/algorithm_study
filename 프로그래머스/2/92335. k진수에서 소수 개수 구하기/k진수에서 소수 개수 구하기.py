def conv_base(n, k):
    result = ""
    while 0 < n // k:
        result += str(n % k)
        n //= k
    result += str(n % k)
    return result[::-1]

def is_prime(n):
    n = int(n)
    if n <= 1:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    n_base_k = conv_base(n, k)
    kn = len(n_base_k)
    
    splited = list(n_base_k.split('0'))
    answer = 0
    for num in splited:
        if num != '' and is_prime(num):
            answer += 1
    return answer
                
