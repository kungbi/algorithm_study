import sys
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(edges, visited, curr):
	n = len(edges) - 1
	for i in range(1, n + 1):
		if edges[curr][i] == 1 and visited[i] == False:
			visited[i] = True
			dfs(edges, visited, i)

	return 1

def solution():
	n, m = map(int, input().split())
	edges = [[0] * (n + 1) for _ in range(n + 1)]

	for _ in range(m):
		u, v = map(int, input().split())
		edges[u][v] = 1
		edges[v][u] = 1

	visited = [False] * (n + 1)
	result = 0
	for i in range(1, n + 1):
		if visited[i] == False:
			visited[i] = True
			dfs(edges, visited, i)
			result += 1
	print(result)
	
	
solution()