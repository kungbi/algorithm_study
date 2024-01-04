def calc(users, emoticons, sale_rates):
    join = 0
    sales = 0
    
    for user in users:
        tmp = 0
        for price, rate in zip(emoticons, sale_rates):
            if user[0] <= rate:
                tmp += price * 0.01 * (100 - rate)
        if user[1] <= tmp:
            join += 1
        else:
            sales += tmp
    return (join, int(sales))

def recursive(users, emoticons, sale_rates, index, result):
    if index == len(sale_rates):
        join, sales = calc(users, emoticons, sale_rates)
        if result[0] < join:
            result[0] = join
            result[1] = sales
        elif result[0] == join and result[1] < sales:
            result[1] = sales
        return 0
    
    for i in range(10, 50, 10):
        sale_rates[index] = i
        recursive(users, emoticons, sale_rates, index + 1, result)
        sale_rates[index] = 0

def solution(users, emoticons):
    sale_rates = [0] * len(emoticons)
    result = [0, 0]
    
    for i in range(10, 50, 10):
        sale_rates[0] = i
        recursive(users, emoticons, sale_rates, 1, result)
        sale_rates[0] = 0
    return result
        