# 연구소
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_origin = []
options = []

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

result = 0

# 초기 바이러스, 벽, 빈칸 구분
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus_origin.append([i, j])
        elif arr[i][j] == 0:
            options.append([i, j])

# 기둥 3선택
for s1 in range(len(options)-2):
    for s2 in range(s1+1, len(options)-1):
        for s3 in range(s2+1, len(options)):
            # 배열 복사
            temp_arr = deepcopy(arr)
            virus = deque(virus_origin)

            # 벽 세우기
            i1, j1 = options[s1]
            i2, j2 = options[s2]
            i3, j3 = options[s3]
            temp_arr[i1][j1] = 1
            temp_arr[i2][j2] = 1
            temp_arr[i3][j3] = 1

            # 바이러스 퍼뜨리기
            while virus:
                cur_i, cur_j = virus.popleft()
                for k in range(4):
                    new_i = cur_i + di[k]
                    new_j = cur_j + dj[k]
                    if 0 <= new_i < N and 0 <= new_j < M:
                        if temp_arr[new_i][new_j] == 0:
                            temp_arr[new_i][new_j] = 2
                            virus.append([new_i, new_j])
                            
            # 안전 영역 계산
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if temp_arr[i][j] == 0:
                        cnt += 1
                        
            result = max(result, cnt)

print(result)