import sys
sys.setrecursionlimit(10**6)


def input():
	return sys.stdin.readline().rstrip()

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

n = None
m = None
dp = None

def is_frame(x, y):
	global n, m
	return 0 <= x < m and 0 <= y < n

def dfs(arr, visited, pos):
	global n, m, dp

	x, y = pos
	if y == n - 1 and x == m - 1:
		return 1
	if dp[y][x] != -1:
		return dp[y][x]

	cnt = 0
	h = arr[y][x]
	for dx, dy in zip(dxs, dys):
		nx = x + dx
		ny = y + dy
		if is_frame(nx, ny) and h > arr[ny][nx]:
			visited[ny][nx] = True
			cnt += dfs(arr, visited, (nx, ny))
			visited[ny][nx] = False
	dp[y][x] = cnt
	return cnt

def solve():
	global n, m, dp

	n, m = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(n)]

	dp = [[-1] * m for _ in range(n)]

	visited = [[0] * m for _ in range(n)]
	visited[0][0] = True
	dfs(arr, visited, (0, 0))
	print(dp[0][0])
	

solve()