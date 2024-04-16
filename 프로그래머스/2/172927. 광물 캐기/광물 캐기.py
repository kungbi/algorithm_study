result = float('inf')
table = [
    {'diamond': 1, 'iron': 1, 'stone': 1},
    {'diamond': 5, 'iron': 1, 'stone': 1},
    {'diamond': 25, 'iron': 5, 'stone': 1},
]

def calc_energy_cost(pick_idx, minerals, mine_idx):
    cnt = 0
    cost = 0
    while mine_idx < len(minerals) and cnt < 5:
        cost += table[pick_idx][minerals[mine_idx]]
        cnt += 1
        mine_idx += 1
    return (mine_idx, cost)

def f(picks, minerals, idx, count):
    global result
    
    if len(minerals) <= idx or sum(picks) == 0:
        result = min(result, count)
        return
    
    for i in range(3):
        if 0 < picks[i]:
            next_idx, cost = calc_energy_cost(i, minerals, idx)
            
            picks[i] -= 1
            f(picks, minerals, next_idx, count + cost)
            picks[i] += 1

def solution(picks, minerals):
    f(picks, minerals, 0, 0)
    return result
