import sys

def input():
    return sys.stdin.readline().rstrip()

def f(stack, target):
    result = 0

    while stack:
        curr = stack.pop()

        if target == '(' and curr == '[':
            return -1
        if target == '[' and curr == '(':
            return -1

        if str(curr) in "([":
            return result if result != 0 else 1

        result += curr
    
    return -1



def main():
    arr = list(reversed(input()))
    stack = []

    while arr:
        curr = arr.pop()

        if curr == ')':
            num = f(stack, '(')
            if num < 0:
                return 0
            stack.append(num * 2)
        elif curr == ']':
            num = f(stack, '[')
            if num < 0:
                return 0
            stack.append(num * 3)
        else:
            stack.append(curr)
    
    result = 0
    for num in stack:
        if str(num) in "([":
            return 0
        result += num
    return result



print(main())
