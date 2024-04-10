import sys
from collections import deque

def input():
	return sys.stdin.readline().rstrip()

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def is_frame(x, y):
	return 0 <= x < 6 and 0 <= y < 12

def destroy(arr, x, y):
	queue = deque([(x, y)])
	visited = [[False] * 6 for _ in range(12)]
	visited[y][x] = True
	color = arr[y][x]
	arr[y][x] = '.'

	while queue:
		x, y = queue.popleft()
		for dx, dy in zip(dxs, dys):
			nx = x + dx
			ny = y + dy
			if is_frame(nx, ny) and visited[ny][nx] == False and arr[ny][nx] == color:
				visited[ny][nx] = True
				arr[ny][nx] = '.'
				queue.append((nx, ny))

def get_same_color_count(arr, x, y):
	if arr[y][x] == '.':
		return 0
	queue = deque([(x, y)])
	visited = [[False] * 6 for _ in range(12)]
	visited[y][x] = True
	color = arr[y][x]
	count = 1

	while queue:
		x, y = queue.popleft()
		for dx, dy in zip(dxs, dys):
			nx = x + dx
			ny = y + dy
			if is_frame(nx, ny) and visited[ny][nx] == False and arr[ny][nx] == color:
				visited[ny][nx] = True
				count += 1
				queue.append((nx, ny))
	return count


def gravity(arr):
	for x in range(6):
		for by in range(11, 0, -1):
			if arr[by][x] != '.':
				continue

			for cy in range(by - 1, -1, -1):
				if arr[cy][x] != '.':
					arr[by][x] = arr[cy][x]
					arr[cy][x] = '.'
					break




def solution():
	arr = [list(input()) for _ in range(12)]
	result = 0
	while True:
		destroy_flag = False
		for y in range(12):
			for x in range(6):
				count = get_same_color_count(arr, x, y)
				if 4 <= count:
					destroy(arr, x, y)
					destroy_flag = True
		gravity(arr)
		if destroy_flag == False:
			break
		else:
			result += 1
	print(result)

solution()