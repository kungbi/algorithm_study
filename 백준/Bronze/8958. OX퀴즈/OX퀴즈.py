n = int(input())

for i in range(n):
    str = input()
    total = 0
    p_score = 0
    for x in str:
        if (x != 'X'):
            p_score += 1
            total += p_score
            continue
        p_score = 0
    print(total)
