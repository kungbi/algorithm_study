def solution(s):
    s = list(s.lower())
    for i in range(len(s)):
        if (i == 0 and s[i] != ' ') or (s[i - 1] == ' ' and s[i] != ' '):
            s[i] = s[i].upper()
    return "".join(s)