

def solution():
  t = int(input())
  n = int(input())
  candy_arr = list(map(int, input().split()))
  if sum(candy_arr) < t:
    print("Padaeng_i Cry")
  else:
    print("Padaeng_i Happy")

solution()