import sys
def input():
  return sys.stdin.readline().rstrip()


def solution():
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  prefix_sum = [0] * (n + 1)

  prefix_sum[0] = arr[0]
  for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
  
  for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    if i == 0:
      print(prefix_sum[j])
    else:
      print(prefix_sum[j] - prefix_sum[i - 1])


solution()