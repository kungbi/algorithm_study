def get_angle(s):
    # 1초당 시침 각도는 30 / 3600 도
    # 1초당 분침 각도는 6 / 60 도
    # 1초당 시침 각도는 6도
    return (s * (30 / 3600)) % 360, (s * (6 / 60)) % 360, (s * 6) % 360


def time2sec(h, m, s):
    return h * 3600 + m * 60 + s


def solution(h1, m1, s1, h2, m2, s2):
    start_s = time2sec(h1, m1, s1)
    end_s = time2sec(h2, m2, s2)

    result = 0
    ha, ma, sa = get_angle(start_s)
    if ha == ma == sa:
        result += 1

    for s in range(start_s, end_s):
        ha, ma, sa = get_angle(s)
        
        if s + 1 == 12 * 3600:
            result += 1
            continue

        if sa < ha < sa + 6:
            result += 1
        if sa < ma < sa + 6:
            result += 1
    return result
