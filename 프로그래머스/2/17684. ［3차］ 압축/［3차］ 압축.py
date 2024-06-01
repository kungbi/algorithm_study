def solution(msg):
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    
    answer = []
    w = c = 0
    while c != len(msg):
        c += 1
        
        if msg[w : c + 1] not in dic:
            dic[msg[w : c + 1]] = len(dic) + 1
            answer.append(dic[msg[w : c]])
            w = c
    answer.append(dic[msg[w : c]])
    return answer
        