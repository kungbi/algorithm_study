from collections import defaultdict

def solution(participant, completion):
    dict = defaultdict(int)
    
    for name in participant:
        dict[name] += 1
    
    for name in completion:
        dict[name] -= 1
        
    for key, val in dict.items():
        if val == 1:
            return key
            
    
    
    