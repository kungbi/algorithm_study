def toBinary(c):
    result = ""
    while c != 0:
        result += str(c % 2)
        c //= 2
    return result[::-1]

def solution(s):
    answer = [0, 0]
    
    while s != "1":
        answer[0] += 1
        answer[1] += s.count('0')
        c = s.count('1')
        s = toBinary(c)
        
    return answer

    
    