def solution(s):
    lst_s = s.split()
    print(lst_s)
    
    max_s = int(lst_s[0])
    min_s = int(lst_s[0])
    
    for i in range(1, len(lst_s)):
        if int(lst_s[i]) > max_s:
            max_s = int(lst_s[i])
        if int(lst_s[i]) < min_s:
            min_s = int(lst_s[i])
    answer = str(min_s) +" "+ str(max_s)

    return answer