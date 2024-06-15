from collections import defaultdict


def solution(str1, str2):
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)
    
    for i in range(1, len(str1)):
        string = str1[i - 1 : i + 1]
        if string.isalpha():
            str1_dict[string.lower()] += 1
            
    for i in range(1, len(str2)):
        string = str2[i - 1 : i + 1]
        if string.isalpha():
            str2_dict[string.lower()] += 1
    
    s = 0
    for key in set(str1_dict.keys()) | set(str2_dict.keys()):
        s += max(str1_dict[key], str2_dict[key])
    p = 0
    for key in set(str1_dict.keys()) | set(str2_dict.keys()):
        p += min(str1_dict[key], str2_dict[key])
            
    print(s, p)
    answer = int((p / s if s != 0 else 1) * 65536)
    print(answer)
    return answer