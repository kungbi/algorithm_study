import sys
import bisect
input = sys.stdin.readline

def solution():
	n = int(input())
	arr = list(map(int, input().split()))
	arr_sorted = sorted(set(arr))

	result = []
	for i in arr:
		x = bisect.bisect_left(arr_sorted, i)
		result.append(x)
	print(*result)
	
solution()