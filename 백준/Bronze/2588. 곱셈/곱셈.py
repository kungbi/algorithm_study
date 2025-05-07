num1 = int(input())
num2 = input()
num3 = num2[::-1]

for idx, c in enumerate(num3):
    print(num1 * int(c))
print(num1 * int(num2))
