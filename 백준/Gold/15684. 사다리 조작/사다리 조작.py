import sys
sys.setrecursionlimit(10**6)

def input():
	return sys.stdin.readline().rstrip()

def is_end(line_arr):
	for x in range(n):
		start = x
		for y in range(h):
			x += line_arr[y][x]
		if start != x:
			return False
	return True

n = 0
h = 0
result = 0
def f(line_arr, pos_list, pos_list_len, depth, index):
	global result

	if is_end(line_arr):
		result = min(result, depth)
		return
	if 3 <= depth or result <= depth:
		return
	for i in range(index, pos_list_len):
		a, b = pos_list[i]
		if not line_arr[a][b] and not line_arr[a][b + 1]:
			line_arr[a][b] = 1
			line_arr[a][b + 1] = -1
			f(line_arr, pos_list, pos_list_len, depth + 1, i + 1)
			line_arr[a][b] = 0
			line_arr[a][b + 1] = 0

def solution():
	global n, m, h, result

	n, m, h = map(int, input().split())
	line_arr = [[0] * n for _ in range(h)]
	for _ in range(m):
		a, b = map(int, input().split())
		line_arr[a - 1][b - 1] = 1
		line_arr[a - 1][b] = -1

	pos_list = []
	pos_list_len = 0
	for a in range(h):
		for b in range(n - 1):
			if line_arr[a][b] == 0 and line_arr[a][b + 1] == 0:
				pos_list.append((a, b))
				pos_list_len += 1
	
	result = 4
	f(line_arr, pos_list, pos_list_len, 0, 0)
	print(result if result < 4 else -1)
	

solution()