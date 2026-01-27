def solution(n, lost, reserve):
    answer = 0
    
    # 도난 당했지만 여벌 체육복이 있는 경우 제외
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for rr in real_reserve:
        if rr-1 in real_lost:
            real_lost.remove(rr-1)

        elif rr+1  in real_lost:
            real_lost.remove(rr+1)
    answer = n - len(real_lost)
    return answer