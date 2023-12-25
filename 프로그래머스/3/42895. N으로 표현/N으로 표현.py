
def calc_sets(a_set, b_set):
    tmp_set = set()
    for a in a_set:
        for b in b_set:
            tmp_set.add(a - b)
            tmp_set.add(a + b)
            tmp_set.add(a * b)
            if b != 0:
                tmp_set.add(a / b)
    return tmp_set

def solution(N, number):
    sets = list()
    sets.append(set())
    for i in range(1, 9):
        tmp_set = set([int(str(N) * i)])
        for j in range(1, i):
            if i - j == j - i:
                continue
            calc_result = calc_sets(sets[i - j], sets[j - i])
            tmp_set = tmp_set.union(calc_result)
        sets.append(tmp_set)
        for j in tmp_set:
            if j == number:
                return i
    return -1