def get(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    return result

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        res = get(i)
        if res % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
        