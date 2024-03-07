import sys
from itertools import combinations

def input():
	return sys.stdin.readline().rstrip()

def calc(arr, S):
	sum = 0
	for pair in combinations(S, 2):
		a, b = pair
		sum += arr[a][b]
		sum += arr[b][a]
	return sum

def solution():
	n = int(input())
	arr = [list(map(int, input().split())) for _ in range(n)]

	result = float('inf')
	A = combinations(range(n), n // 2)
	for a in A:
		b = tuple(set(range(n)) - set(a))
		a_score = calc(arr, a)
		b_score = calc(arr, b)

		result = min(result, abs(a_score - b_score))
	print(result)

solution()
