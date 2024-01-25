import math

def solution():
	n, k = map(int, input().split())
	print(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)) )

solution()