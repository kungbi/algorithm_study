MAX = 1_000_000


def solution(edges):
    # [1, 0] 1나가기 0들어옴.
    inout_arr = [[0, 0] for _ in range(MAX + 1)]
    
    max_i = -1
    max_v = 0
    for edge in edges:
        a, b = edge
        inout_arr[a][0] += 1
        inout_arr[b][1] += 1

    a_i = 0
    a = b = c = 0
    for i in range(len(inout_arr)):
        if 1 < inout_arr[i][0] and inout_arr[i][1] == 0: # 정점
            a = inout_arr[i][0]
            a_i = i
        elif inout_arr[i][0] == 0 and inout_arr[i][1] != 0: # 막대
            b += 1
        elif inout_arr[i][0] == 2 and 2 <= inout_arr[i][1]: # 도넛
            c += 1
    
    a -= b + c
    return [a_i, a, b, c]
