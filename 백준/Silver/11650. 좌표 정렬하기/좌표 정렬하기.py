

def solution():
	n = int(input())
	pos_list = []
	for i in range(n):
		x, y = map(int, input().split())
		pos_list.append([x, y])
	
	pos_list.sort(key=lambda x: (x[0], x[1]))
	for pos in pos_list:
		print(*pos)


solution()