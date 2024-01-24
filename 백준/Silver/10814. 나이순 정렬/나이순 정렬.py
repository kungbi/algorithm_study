

def solution():
	n = int(input())
	users = []
	for i in range(n):
		age, name = input().split()
		age = int(age)
		users.append([i, age, name])
	
	users.sort(key=lambda x: (x[1], x[0]))
	for user in users:
		print(user[1], user[2])


solution()