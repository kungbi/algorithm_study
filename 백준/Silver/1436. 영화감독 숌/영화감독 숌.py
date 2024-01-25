
def is_666(num):
	num = str(num)
	stack = 0
	for c in num:
		if c == '6':
			stack += 1
		else:
			stack = 0

		if stack == 3:
			return True
	return False

def solution():
	n = int(input())
	num = 0
	count = 0

	while True:
		if is_666(num):
			count += 1
			if count == n:
				break
		num += 1
	print(num)


solution()