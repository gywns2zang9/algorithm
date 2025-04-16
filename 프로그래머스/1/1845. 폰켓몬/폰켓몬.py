def solution(nums):
    n = len(nums) // 2 # 가져갈 폰켓몬 수
    
    set_nums = set(nums)
    
    if n >= len(set_nums):
        answer = len(set_nums)
    else:
        answer = n
    return answer