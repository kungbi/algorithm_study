def get_parent(disjoint, idx):
    if disjoint[idx] != idx:
        disjoint[idx] = get_parent(disjoint, disjoint[idx])
    return disjoint[idx]

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    visited = [False] * n
    disjoint = [i for i in range(n)]
    
    answer = 0
    for cost in costs:
        a, b, c = cost
        print(cost)
        
        a_parent = get_parent(disjoint, a)
        b_parent = get_parent(disjoint, b)
        
        if a_parent != b_parent:
            disjoint[a_parent] = b_parent
            answer += c
        print(disjoint)
        
    return answer

# 0 - 1 - 2 - 3
# 0, 1, 5
# 2, 3, 1
# 0, 2, 1
# 1, 3, 1