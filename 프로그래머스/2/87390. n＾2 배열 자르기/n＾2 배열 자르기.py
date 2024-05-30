def solution(n, left, right):
    answer = []
    for x in range(left, right + 1):
        i = x // n + 1
        j = x % n + 1
        if j <= i:
            answer.append(i)
        else:
            answer.append(j)
    return answer
        