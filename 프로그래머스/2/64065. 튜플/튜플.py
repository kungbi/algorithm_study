def isnum(c):
    return ord('0') <= ord(c) <= ord('9')

def getint(str, start):
    i = start
    while isnum(str[i]):
        i += 1
    end = i
    return (end - start, int(str[start:end]))
    

def str2list(s):
    s = s[1: -1]
    result = []
    buffer = []
    
    i = 0
    while i < len(s):
        if s[i] == '{':
            buffer = []
        elif s[i] == '}':
            result.append(buffer)
        elif isnum(s[i]):
            length, num = getint(s, i)
            i += length -1 
            buffer.append(num)
        i += 1
    return result


def solution(s):
    s_list = str2list(s)
    s_list.sort(key=lambda x: len(x))

    result = []
    tmp = set()
    for item in s_list:
        result.append(list(set(item) - tmp)[0])
        tmp = tmp | set(item)
    return result
        
            
            