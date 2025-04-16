def solution(bandage, health, attacks):
    answer = 0
    
    bandage_time = bandage[0] # 1부터 50
    bandage_heal = bandage[1] # 1부터 100
    bandage_bonus = bandage[2] # 1부터 100
    
    max_health = health
    
    t = 0
    
    for attack in attacks:
        attack_time = attack[0]
        attack_damage = attack[1]
        
        cnt = 0
        while t < attack_time:
            t += 1
            if t == attack_time:
                break
            cnt += 1
            health += bandage_heal
            if cnt == bandage_time:
                cnt = 0
                health += bandage_bonus
            
            if health > max_health:
                health = max_health
            print(t, health)
        
        health -= attack_damage
        if health <= 0:
            answer = -1
            break
    
    if health > 0:
        answer = health
    
    return answer