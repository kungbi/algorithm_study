def solution(bandage, health, attacks):
    attacks.reverse()
    
    t = 0
    max_health = health
    heal_cnt = damage_cnt = attack_damage = 0
    while 0 < health and attacks:
        if attacks[-1][0] == t:
            attack_damage = attacks.pop()[1]
            health -= attack_damage
            heal_cnt = 0
        else:
            heal_cnt += 1
            health += bandage[1]
            if heal_cnt == bandage[0]:
                health += bandage[2]
                heal_cnt = 0
            if max_health < health:
                health = max_health
                
        t += 1
    if 0 < health:
        return health
    return -1