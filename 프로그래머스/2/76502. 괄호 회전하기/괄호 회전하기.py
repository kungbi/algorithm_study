from collections import deque

def is_correct(s):
    stack = []
    for i in range(len(s)):
        if s[i] in "[{(":
            stack.append(s[i])
        elif stack:
            if s[i] == ']' and stack[-1] != '[':
                return False
            elif s[i] == '}' and stack[-1] != '{':
                return False
            elif s[i] == ')' and stack[-1] != '(':
                return False
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True
            

def solution(s):
    s = deque(list(s))
    answer = 0

    for _ in range(len(s)):
        answer += 1 if is_correct(s) else 0
        s.append(s.popleft())
        
        
    return answer