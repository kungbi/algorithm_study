from collections import defaultdict

def solution(friends, gifts):
    friends_len = len(friends)
    
    pre_gift_map = [[0] * friends_len for _ in range(friends_len)]
    next_gift_map = [0] * friends_len
    gift_index = [0] * friends_len
    
    f_idx = dict()
    for i in range(friends_len):
        f_idx[friends[i]] = i
        
    for gift in gifts:
        g_from, g_to = gift.split()
        g_from_idx = f_idx[g_from]
        g_to_idx = f_idx[g_to]
        pre_gift_map[g_from_idx][g_to_idx] += 1
        gift_index[g_from_idx] += 1
        gift_index[g_to_idx] -= 1
        
    for friend_a in range(friends_len):
        for friend_b in range(friend_a + 1, friends_len):
            from_a = pre_gift_map[friend_a][friend_b]
            from_b = pre_gift_map[friend_b][friend_a]
            a_idx = gift_index[friend_a]
            b_idx = gift_index[friend_b]
            
            if from_a < from_b:
                next_gift_map[friend_b] += 1
            elif from_a > from_b:
                next_gift_map[friend_a] += 1
            elif a_idx < b_idx:
                next_gift_map[friend_b] += 1
            elif a_idx > b_idx:
                next_gift_map[friend_a] += 1
    
    return max(next_gift_map) 
        
                
    
    
    