from collections import defaultdict

def solution(edges):
    result = [0, 0, 0, 0]
    n = 0
    inout_map = dict()
    for edge in edges:
        if edge[0] not in inout_map:
            inout_map[edge[0]] = [0, 0]
        if edge[1] not in inout_map:
            inout_map[edge[1]] = [0, 0]
        
        inout_map[edge[0]][0] += 1
        inout_map[edge[1]][1] += 1
    
    for v, inout in inout_map.items():
        if 2 <= inout[0] and inout[1] == 0:
            result[0] = v
            n = inout[0]
        elif inout[0] == 2 and 2 <= inout[1]:
            result[3] += 1
        elif inout[0] == 0 and inout[1]:
            result[2] += 1
    result[1] = n - result[2] - result[3]
    return result
    
    