def solution(n):
    i = 1
    while i * i <= n:
        if i* i == n:
            return (i + 1) ** 2
        i += 1
    return -1