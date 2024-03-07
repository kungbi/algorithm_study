import sys
sys.setrecursionlimit(10**6)

def input():
	return sys.stdin.readline().rstrip()

def f(A, op, i, num):
	global result, n

	if i == n:
		result[0] = max(result[0], num)
		result[1] = min(result[1], num)
		return
	
	for j in range(4):
		for _ in range(op[j]):
			op[j] -= 1
			if j == 0:
				f(A, op, i + 1, num + A[i])
			elif j == 1:
				f(A, op, i + 1, num - A[i])
			elif j == 2:
				f(A, op, i + 1, num * A[i])
			elif j == 3:
				if num < 0:
					f(A, op, i + 1, -(-num // A[i]))
				else:
					f(A, op, i + 1, num // A[i])
			op[j] += 1

n = 0
result = [float('-inf'), float('inf')]
def solution():
	global result, n

	n = int(input())
	A = list(map(int, input().split()))
	op = list(map(int, input().split()))

	f(A, op, 1, A[0])
	print(result[0])
	print(result[1])


solution()
