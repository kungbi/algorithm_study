
def conv_base(n, num):
    base = "0123456789ABCDEF"
    if n <= num:
        return conv_base(n, num // n) + base[num % n]
    return base[num % n]

def get_next_num(n, num):
    curr_num = int(num, n) + 1
    return conv_base(n, curr_num)

def solution(n, t, m, p):
    answer = "0"
    answer_len = 1
    curr_num = '0'

    while answer_len <= t * m:
        curr_num = get_next_num(n, curr_num)
        answer += curr_num
        answer_len += len(curr_num)
        
    result = ""
    i = 0
    while i < t * m:
        if i % m == p - 1:
            result += answer[i]
        i += 1
    return result