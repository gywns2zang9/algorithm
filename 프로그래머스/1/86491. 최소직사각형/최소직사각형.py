def solution(sizes):
    answer = 0
    A= []
    B= []
    
    for size in sizes:
        a = max(size[0], size[1])
        b = min(size[0], size[1])
        
        A.append(a)
        B.append(b)
    answer = max(A)*max(B)
    
    return answer