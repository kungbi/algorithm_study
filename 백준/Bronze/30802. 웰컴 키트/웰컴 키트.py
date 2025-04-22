n = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())

answer_t = 0
for num in arr:
    answer_t += num // T
    if num % T != 0:
        answer_t += 1

print(answer_t)
print(n // P, n % P)
