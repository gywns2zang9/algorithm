def solution(answers):
    answer = []
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == A[i%5]:
            scores[0] += 1
        if answers[i] == B[i%8]:
            scores[1] += 1
        if answers[i] == C[i%10]:
            scores[2] += 1
    
    if scores[0] == scores[1] == scores[2]:
        answer = [1, 2, 3]
    elif max(scores) == scores[0] == scores[1]:
        answer = [1, 2]
    elif max(scores) == scores[0] == scores[2]:
        answer = [1, 3]
    elif max(scores) == scores[1] == scores[2]:
        answer = [2, 3]
    elif max(scores) == scores[0]:
        answer = [1]
    elif max(scores) == scores[1]:
        answer = [2]
    elif max(scores) == scores[2]:
        answer = [3]
    return answer