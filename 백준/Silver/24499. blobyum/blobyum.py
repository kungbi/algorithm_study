

def solution():
  n, k = tuple(map(int, input().split()))
  arr = list(map(int, input().split())) * 2
  dp = [0] * (n * 2)
  dp[0] = arr[0]
  for i in range(1, n * 2):
    dp[i] = dp[i-1] + arr[i]

  result = 0
  for i in range(n):
    j = i + k
    result = max(result, dp[j] - dp[i])
  print(result)


solution()