h, m = map(int, input().split())

time = h * 60 + m
time -= 45

if time < 0:
  time = 24 * 60 + time

print(time // 60, time % 60)