def solution(n, lost, reserve):
    answer = n - len(lost) # 체육복이 있는 학생 수
    
    for l in lost:
        if l in reserve:
            reserve.remove(l-1)
            answer += 1
            
        elif l > 1 and l-1 in reserve:
            reserve.remove(l-1)
            answer += 1
        elif n > l and l+1 in reserve:
            reserve.remove(l+1)
            answer += 1
    return answer