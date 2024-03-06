import sys
sys.setrecursionlimit(10**6)
from copy import deepcopy

def input():
	return sys.stdin.readline().rstrip()

def move_left(arr, n):
	for y in range(n):
		cursor = 0
		for i in range(n):
			tmp = arr[y][i]
			if tmp == 0:
				continue

			arr[y][i] = 0
			if arr[y][cursor] == 0:
				arr[y][cursor] = tmp
			elif arr[y][cursor] == tmp:
				arr[y][cursor] = tmp * 2
				cursor += 1
			else:
				cursor += 1
				arr[y][cursor] = tmp

def move_right(arr, n):
	for y in range(n):
		cursor = n - 1
		for i in range(n):
			tmp = arr[y][n - 1 - i]
			if tmp == 0:
				continue

			arr[y][n - 1 - i] = 0
			if arr[y][cursor] == 0:
				arr[y][cursor] = tmp
			elif arr[y][cursor] == tmp:
				arr[y][cursor] = tmp * 2
				cursor -= 1
			else:
				cursor -= 1
				arr[y][cursor] = tmp


def move_down(arr, n):
	for x in range(n):
		cursor = n - 1
		for i in range(n):
			tmp = arr[n - 1 - i][x]
			if tmp == 0:
				continue

			arr[n - 1 - i][x] = 0
			if arr[cursor][x] == 0:
				arr[cursor][x] = tmp
			elif arr[cursor][x] == tmp:
				arr[cursor][x] = tmp * 2
				cursor -= 1
			else:
				cursor -= 1
				arr[cursor][x] = tmp

def move_up(arr, n):
	for x in range(n):
		cursor = 0
		for i in range(n):
			tmp = arr[i][x]
			if tmp == 0:
				continue

			arr[i][x] = 0
			if arr[cursor][x] == 0:
				arr[cursor][x] = tmp
			elif arr[cursor][x] == tmp:
				arr[cursor][x] = tmp * 2
				cursor += 1
			else:
				cursor += 1
				arr[cursor][x] = tmp

def f(arr, dir, depth):
	global result, n

	if depth == 5:
		for y in range(n):
			for x in range(n):
				result = max(result, arr[y][x])
		return

	n = len(arr)
	for i in range(4):
		arr_tmp = deepcopy(arr)
		if i == 0:
			move_left(arr_tmp, n)
		elif i == 1:
			move_up(arr_tmp, n)
		elif i == 2:
			move_right(arr_tmp, n)
		elif i == 3:
			move_down(arr_tmp, n)
		f(arr_tmp, dir, depth + 1)


n = 0
result = 0
def solution():
	global result, n

	n = int(input())
	arr = [list(map(int, input().split())) for _ in range(n)]

	f(arr, 0, 0)
	print(result)


solution()