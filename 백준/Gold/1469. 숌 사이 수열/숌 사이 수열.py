from copy import deepcopy

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

dp = [-1] * 2 * n
visited = [False] * n

def is_full(arr):
	for num in arr:
		if num == -1:
			return -1
	return 1

def f(dp, visited, p, i):
	while i < 2 * n and dp[i] != -1:
		i += 1

	next_i = i + arr[p] + 1
	if 2 * n <= next_i or (dp[i] != -1 and dp[next_i] != -1):
		return -1

	dp[i] = dp[next_i] = arr[p]
	visited[p] = True

	for j in range(n):
		if visited[j] == False:
			result = f(deepcopy(dp), deepcopy(visited), j, i + 1)
			if result == 1:
				return 1

	if is_full(dp) == 1:
		print(*dp)
		return 1
	return -1

def solution():
	for i in range(n):
		if f(deepcopy(dp), deepcopy(visited), i, 0) == 1:
			return 0
	print(-1)

solution()
