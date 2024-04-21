def f(n, a, b, count):
    # if (a - 1) // 2 + 1 == (b - 1) // 2 + 1:
    #     return count + 1
    if a == b:
        return count
    return f(n // 2, (a - 1) // 2 + 1, (b - 1) // 2 + 1, count + 1)
    

def solution(n,a,b):
    
    return f(n, a, b, 0)