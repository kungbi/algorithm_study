import sys
def input():
    return sys.stdin.readline().rstrip()


def solution():
    input_str = input()
    tmp = ""
    arr = []
    for i in range(len(input_str)):
        if input_str[i] == '-' or input_str[i] == '+':
            arr.append(int(tmp))
            arr.append(input_str[i])
            tmp = ""
        else:
            tmp += input_str[i]
    arr.append(int(tmp))

    result = arr[0]
    minus = False
    tmp = 0
    for i in range(1, len(arr)):
        if arr[i] == '-':
            if minus == True:
                result -= tmp
            else:
                result += tmp
            minus = True
            tmp = 0
        elif arr[i] != '+':
            tmp += arr[i]
    if minus == True:
        result -= tmp
    else:
        result += tmp
    print(result)


    

solution()