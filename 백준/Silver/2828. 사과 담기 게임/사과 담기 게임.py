import sys

def input():
	return sys.stdin.readline().rstrip()

def solution():
	N, M = map(int, input().split())
	pos = 1

	J = int(input())
	result = 0
	for _ in range(J):
		x = int(input())
		if pos <= x <= pos + M - 1:
			continue
		num = 0
		if x < pos:
			num = pos - x
			pos -= num
		elif pos + M - 1 < x:
			num = x - (pos + M - 1)
			pos += num
		result += num
	return result

print(solution())