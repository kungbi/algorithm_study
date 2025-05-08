import sys

T = int(input())

for _ in range(T):
    wears = dict()
    n = int(input())
    for _ in range(n):
        name, type = input().split()
        if type in wears:
            wears[type].append(name)
        else:
            wears[type] = [name]

    cnt = 1

    for x in wears:
        cnt *= len(wears[x]) + 1
    print(cnt - 1)
