import sys
sys.setrecursionlimit(10**6)

def input():
	return sys.stdin.readline().rstrip()

result = 0
def f(arr, i, n, money):
	global result

	result = max(result, money)

	for j in range(i, n):
		t, m = arr[j]
		if j + t - 1 < n:
			f(arr, j + t, n, money + m)

def solution():
	global result

	n = int(input())
	arr = []

	for _ in range(n):
		arr.append(tuple(map(int, input().split())))
	
	f(arr, 0, n, 0)
	print(result)


solution()