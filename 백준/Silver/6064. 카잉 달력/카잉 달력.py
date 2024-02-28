import sys
def input():
	return sys.stdin.readline().rstrip()

def solution():
	T = int(input())
	for _ in range(T):
		M, N, X, Y = map(int, input().split())
		
		i = X
		flag = False
		while i <= M * N:
			if (i - X) % M == 0 and (i - Y) % N == 0:
				flag = True
				break
			i += M
		if flag:
			print(i)
		else:
			print(-1)


solution()