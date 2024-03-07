import sys
from copy import deepcopy
sys.setrecursionlimit(10**6)

def input():
	return sys.stdin.readline().rstrip()

def is_frame(x, y, n, m):
	return 0 <= x < m and 0 <= y < n

def fill_up(arr, pos, n, m):
	x, y = pos
	for i in range(1, n):
		ny = y - i
		if not is_frame(x, ny, n, m):
			break
		if arr[ny][x] == 6:
			break
		if 1 <= arr[ny][x] <= 5:
			continue
		arr[ny][x] = 7

def fill_down(arr, pos, n, m):
	x, y = pos
	for i in range(1, n):
		ny = y + i
		if not is_frame(x, ny, n, m):
			break
		if arr[ny][x] == 6:
			break
		if 1 <= arr[ny][x] <= 5:
			continue
		arr[ny][x] = 7

def fill_left(arr, pos, n, m):
	x, y = pos
	for i in range(1, m):
		nx = x - i
		if not is_frame(nx, y, n, m):
			break
		if arr[y][nx] == 6:
			break
		if 1 <= arr[y][nx] <= 5:
			continue
		arr[y][nx] = 7

def fill_right(arr, pos, n, m):
	x, y = pos
	for i in range(1, m):
		nx = x + i
		if not is_frame(nx, y, n, m):
			break
		if arr[y][nx] == 6:
			break
		if 1 <= arr[y][nx] <= 5:
			continue
		arr[y][nx] = 7


cctv_dir = [[], [2], [0, 2], [1, 2], [0, 1, 2], [0, 1, 2, 3]]

def f(arr, cctv_list, i, n, m):
	global empty_cnt, result, cctv_dir

	if i == len(cctv_list):
		sum = 0
		for y in range(n):
			for x in range(m):
				if arr[y][x] == 0:
					sum += 1
		result = min(result, sum)
		return

	x, y, c = cctv_list[i]
	cctv_dir_tmp = deepcopy(cctv_dir[c])
	for _ in range(4): # 4개 방향
		arr_tmp = deepcopy(arr)

		# 번호에 해당하는 fill 함수 부르기
		for dir in cctv_dir_tmp:
			if dir == 0:
				fill_left(arr_tmp, (x, y), n, m)
			if dir == 1:
				fill_up(arr_tmp, (x, y), n, m)
			if dir == 2:
				fill_right(arr_tmp, (x, y), n, m)
			if dir == 3:
				fill_down(arr_tmp, (x, y), n, m)
		
		# 다른 cctv
		f(arr_tmp, cctv_list, i + 1, n, m)

		# 1. 방향 돌리기
		for j in range(len(cctv_dir_tmp)):
			cctv_dir_tmp[j] = (cctv_dir_tmp[j] + 1) % 4


empty_cnt = 0
result = float('inf')
def solution():
	global result, empty_cnt

	n, m = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(n)]

	cctv_list = []
	for y in range(n):
		for x in range(m):
			if 1 <= arr[y][x] <= 5:
				cctv_list.append([x, y, arr[y][x]])
			elif arr[y][x] == 0:
				empty_cnt += 1

	f(arr, cctv_list, 0, n, m)
	print(result)

solution()