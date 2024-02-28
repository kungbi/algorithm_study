import sys
from collections import deque

def input():
	return sys.stdin.readline().rstrip()

def D(num):
	return (num * 2) % 10000

def S(num):
	return (num - 1) % 10000

def S2(num):
	if num == 0:
		return 9999
	return num - 1

def L(num):
	return (num % 1000) * 10 + num // 1000

def R(num):
	return (num % 10) * 1000 + num // 10

def f(A, B):
	queue = deque([(A, "")])

	visited = [False] * 10000
	visited[A] = True

	while queue:
		num, commands = queue.popleft()

		if num == B:
			return commands
		
		tmp = D(num)
		if visited[tmp] == False:
			visited[tmp] = True
			queue.append((tmp, commands + 'D'))

		tmp = S(num)
		if visited[tmp] == False:
			visited[tmp] = True
			queue.append((tmp, commands + 'S'))

		tmp = L(num)
		if visited[tmp] == False:
			visited[tmp] = True
			queue.append((tmp, commands + 'L'))

		tmp = R(num)
		if visited[tmp] == False:
			visited[tmp] = True
			queue.append((tmp, commands + 'R'))


def solution():
	T = int(input())
	for _ in range(T):
		A, B = map(int, input().split())
		print(f(A, B))

solution()