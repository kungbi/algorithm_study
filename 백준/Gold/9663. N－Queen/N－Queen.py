import sys

def input():
	return sys.stdin.readline().rstrip()

def is_frame(x, y, n):
	return 0 <= x < n and 0 <= y < n

def is_possible(arr, pos):
	x, y = pos
	for pos_queen in arr:
		q_x, q_y = pos_queen
		if x == q_x or y == q_y:
			return False
		if abs(x - q_x) == abs(y - q_y):
			return False
	return True

def f(arr, y, n):
	global visited_col

	if y == n:
		return 1

	cnt = 0
	for x in range(n):
		if visited_col[x] == True:
			continue

		if is_possible(arr, (x, y)):
			arr.append((x, y))
			visited_col[x] = True
			cnt += f(arr, y + 1, n)
			arr.pop()
			visited_col[x] = False
		
	return cnt

visited_col = []
def solution():
	global visited_col

	n = int(input())
	arr = []
	visited_col = [False] * n
	print(f(arr, 0, n))

solution()