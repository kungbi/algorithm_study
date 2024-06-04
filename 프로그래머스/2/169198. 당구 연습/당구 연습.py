from math import sqrt

def calc_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solution(m, n, startX, startY, balls):
    answer = []
    start_pos = (startX, startY)
    
    for ball in balls:
        tmp = float('inf')
        
        if startX != ball[0] or not ball[1] < startY:
            tmp = min(tmp, calc_dist((ball[0], ball[1] * -1), start_pos))
        if startX != ball[0] or not startY < ball[1]:
            tmp = min(tmp, calc_dist((ball[0], 2 * n - ball[1]), start_pos))
        if startY != ball[1] or not ball[0] < startX:
            tmp = min(tmp, calc_dist((ball[0] * -1, ball[1]), start_pos))
        if startY != ball[1] or not startX < ball[0]:
            tmp = min(tmp, calc_dist((2 * m - ball[0], ball[1]), start_pos))
        answer.append(tmp)
    
    return answer