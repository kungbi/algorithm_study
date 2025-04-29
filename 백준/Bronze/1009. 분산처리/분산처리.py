import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    last = a % 10
    res = pow(last, b, 10)
    print(res or 10)
