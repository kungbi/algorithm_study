import sys

def input():
	return sys.stdin.readline().rstrip()


def solve():
	n = int(input())
	k = int(input())

	if (n // 2 < k):
		return 0

	dp = [[0] * n for _ in range(k)]
	for i in range(n):
		dp[0][i] = 1
	for t in range(1, k):
		for i in range(n - 1, 0, -1):
			if i + 2 < n:
				dp[t][i] = (dp[t][i + 1] + dp[t-1][i + 2]) % 1_000_000_003 

	tmp = sum(dp[k-1])
	if 1 < k:
		return (tmp + dp[k-1][1])
	return tmp


print(solve() % 1_000_000_003)