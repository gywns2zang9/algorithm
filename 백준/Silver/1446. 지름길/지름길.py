# 지름길
N, D = map(int, input().split()) # N = 지름길 수, D = 고속도로 길이
# arr = [list(map(int, input().split())) for _ in range(N)] # 시작 위치, 도착 위치, 지름길 길이
arr = []
for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D and d <= (e-s):
        arr.append([s, e, d])
arr.sort()
# print(arr)
# 근데 먼저 온다고 지름길을 타도되나?
# 근데 또 12개를 on/off 하면 2**12 = 4096 갠데 다 봐도 될듯?

min_D = D
len_arr = len(arr)

def dfs(index, position, now_D):
    global min_D, len_arr
    # 
    if index > len_arr - 1:
        min_D = min(min_D, now_D + D-position)
        return

    now_s, now_e, now_d = arr[index]
    # position은 현재 내 위치
    if position > now_s: # 지름길 지나갔으면 다음거로
        return dfs(index+1, position, now_D)

    if index == len_arr - 1: # 마지막 지름길
        now_D = now_D + ((now_s-position)+ now_d + (D- now_e))
        min_D = min(min_D, now_D)
        return

    else:
        if now_D > min_D: # 이미 넘으면 끝내기
            return

        # case1: now 지름길 이용함
        # case2: now 지름길 이용안함
        return dfs(index+1, now_e, (now_s-position) + now_D+now_d), dfs(index+1, position, now_D)

dfs(0, 0, 0)
print(min_D)