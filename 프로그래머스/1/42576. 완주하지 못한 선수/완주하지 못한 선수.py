def solution(participant, completion):

    participant.sort()
    completion.sort()
    i = -1
    max_i = len(completion)

    while True:
        i += 1
        if i == max_i:
                answer = participant[i]
                break 
        
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer