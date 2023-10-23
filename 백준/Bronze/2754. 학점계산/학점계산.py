
str = input()


def to_number(str):
    score = 0
    if (str[0] == 'A'):
        score += 4.0
    elif (str[0] == 'B'):
        score += 3.0
    elif (str[0] == 'C'):
        score += 2.0
    elif (str[0] == 'D'):
        score += 1.0
    elif (str[0] == 'F'):
        return (0.0)

    if (str[1] == '+'):
        score += 0.3
    elif (str[1] == '-'):
        score -= 0.3
    return (score)


print(to_number(str))
