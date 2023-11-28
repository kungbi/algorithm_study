def replace_sec(h, m, s):
    re = h * 3600 + m * 60 + s
    return re


def replace_angle(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = (sec % 3600) % 60
    sec_angle = float(s * 6) % 360
    min_angle = ((m * 6) + (s / 10)) % 360
    hour_angle = ((h * 30) + (m / 2) + (s / 120)) % 360
    return (hour_angle, min_angle, sec_angle)


def solution(h1, m1, s1, h2, m2, s2):
    count = 0

    # past_h, past_m, past_s = replace_angle(replace_sec(h1, m1, s1))
    past_h = past_m = past_s = 0
    for i in range(replace_sec(h1, m1, s1), replace_sec(h2, m2, s2) + 1):
        curr_h, curr_m, curr_s = replace_angle(i)
        tmp = 0

        if past_s < past_h and curr_h < curr_s:
            tmp += 1
        elif past_s < past_h and curr_s == 0:
            tmp += 1
        elif curr_h == curr_s:
            tmp += 1

        if past_s < past_m and curr_m < curr_s:
            tmp += 1
        elif past_s < past_m and curr_s == 0:
            tmp += 1
        elif curr_m == curr_s:
            tmp += 1

        if i == 0:
            count += 1
            continue

        if i != 3600 * 12:
            count += tmp
        else:
            count += 1

        past_h, past_m, past_s = curr_h, curr_m, curr_s
    return count


count = solution(0, 0, 0, 23, 59, 59)
print(count)
