LINF = 1e18

n = int(input())
start_y, end_x = map(int, input().split())
lines = []
for _ in range(n):
    x, yl, yh = map(int, input().split())
    lines.append((x, yl, yh))

lines.sort()

s = [(start_y, 0)]

for x, yl, yh in lines:
    new_s = []
    cand_top = LINF
    cand_bottom = LINF
    for y, cost in s:
        if yl <= y <= yh:
            cand_top = min(cand_top, cost + (yh - y))
            cand_bottom = min(cand_bottom, cost + (y - yl))
        else:
            new_s.append((y, cost))
    new_s.append((yh, cand_top))
    new_s.append((yl, cand_bottom))
    s = new_s

# 필요할 때마다 정렬을 수행합니다.
s.sort()

min_h = LINF
cnt_min = 0
for y, cost in s:
    if cost < min_h:
        min_h = cost
        cnt_min = 1
    elif cost == min_h:
        cnt_min += 1

print(end_x + min_h)
print(cnt_min, end=" ")
for y, cost in s:
    if cost == min_h:
        print(y, end=" ")
