from collections import defaultdict

def solution(n, words):
    counter = defaultdict(int)
    counter[words[0]] += 1
    
    wrong = False
    i = 1
    while i < len(words):
        if counter[words[i]] != 0:
            wrong = True
            break
            
        if words[i - 1][-1] != words[i][0]:
            wrong = True
            break
        
        counter[words[i]] += 1
        i += 1
    
    if wrong == False:
        return [0, 0]
    
    return [i % n + 1, i // n + 1 ]
    
    