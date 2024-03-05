import sys

def input():
	return sys.stdin.readline().rstrip()

result = 0

def f(arr, curr, n):
	global result

	if curr == n:
		t_cnt = 0
		for i in range(n):
			h_cnt = 0
			for j in range(n):
				if arr[j] & (1 << i):
					h_cnt += 1
			t_cnt += min(h_cnt, n - h_cnt)
		result = min(result, t_cnt)
		return

	arr[curr] ^= (2**n) - 1
	f(arr, curr + 1, n)
	arr[curr] ^= (2**n) - 1
	f(arr, curr + 1, n)

def solution():
	global result
	N = int(input())
	bit_arr = [0] * N
	result = float('inf')

	for i in range(N):
		for c in input():
			if c == 'H':
				bit_arr[i] = (bit_arr[i] << 1) + 1
			elif c == 'T':
				bit_arr[i] = bit_arr[i] << 1

	f(bit_arr, 0, N)
	return result

print(solution())