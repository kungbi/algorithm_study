
N = int(input())

# 첫 번째 for문 반복 횟수: N번
for i in range(1, N+1):
  # 두 번째 for문 반복 횟수: i번
  for j in range(i):
    print("*", end='')
  print()
