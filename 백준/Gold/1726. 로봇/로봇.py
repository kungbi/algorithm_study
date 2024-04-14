import sys
from collections import deque


def input():
	return sys.stdin.readline().rstrip()


def rotate(dir, command):
	if command == "L":
		if dir == 1: # 동
			return 4
		elif dir == 2: # 서
			return 3
		elif dir == 3: # 남
			return 1
		elif dir == 4: # 북
			return 2
	elif command == "R":
		if dir == 1: # 동 
			return 3
		elif dir == 2: # 서 
			return 4
		elif dir == 3: # 남 
			return 2
		elif dir == 4: # 북 
			return 1

dxs = [0, 1, -1, 0, 0]
dys = [0, 0, 0, 1, -1]


def is_frame(x, y):
	return 0 <= x < m and 0 <= y < n


def bfs(arr, start, end):
	queue = deque([start + (0,)])
	visited = [[[False] * 5 for _ in range(m)] for _ in range(n)]
	visited[start[1]][start[0]][start[2]] = True

	while queue:
		x, y, dir, cost = queue.popleft()
		if (x, y, dir) == (end[0], end[1], end[2]):
			return cost
		nx = x
		ny = y

		for i in range(3):
			nx = nx + dxs[dir]
			ny = ny + dys[dir]
			if not is_frame(nx, ny):
				break
			if arr[ny][nx] == 1:
				break
			if visited[ny][nx][dir] == True:
				continue
			
			visited[ny][nx][dir] = True
			queue.append((nx, ny, dir, cost + 1))

		left_dir = rotate(dir, "L")
		right_dir = rotate(dir, "R")
		if visited[y][x][left_dir] == False:
			visited[y][x][left_dir] = True
			queue.append((x, y, left_dir, cost + 1))
		if visited[y][x][right_dir] == False:
			visited[y][x][right_dir] = True
			queue.append((x, y, right_dir, cost + 1))


n = m = 0


def solution():
	global n, m

	n, m = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(n)]
	start = tuple(map(int, input().split()))
	start = (start[1] - 1, start[0] - 1, start[2])

	end = tuple(map(int, input().split()))
	end = (end[1] - 1, end[0] - 1, end[2])
	print(bfs(arr, start, end))


solution()
