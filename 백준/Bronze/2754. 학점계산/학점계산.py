
str = input()

def to_number(str):
    score = 4.0 - (ord(str[0]) - ord('A'))
    if (score < 0):
        return (0.0)
    if (str[1] == '+'):
        score += 0.3
    elif (str[1] == '-'):
        score -= 0.3
    if (score < 0):
        score = 0.0
    return (score)

print(to_number(str))