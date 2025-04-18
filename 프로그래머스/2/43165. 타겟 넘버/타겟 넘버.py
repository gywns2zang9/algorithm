cnt = 0
def dfs(numbers, now_i, now_sum, target):
    global cnt
    if len(numbers) == now_i:
        if now_sum == target:
            cnt += 1
        return
    else:
        return dfs(numbers, now_i+1, now_sum+numbers[now_i], target), dfs(numbers, now_i+1, now_sum-numbers[now_i], target)
        
        
def solution(numbers, target):
    answer = 0
    dfs(numbers, 1, numbers[0], target)
    dfs(numbers, 1, -numbers[0], target)
    global cnt
    answer = cnt
    return answer