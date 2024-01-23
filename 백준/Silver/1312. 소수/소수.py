
def solution():
  a, b, c = tuple(map(int, input().split()))
  
  for i in range(c):
    a %= b
    a *= 10
  print(a // b)

solution()