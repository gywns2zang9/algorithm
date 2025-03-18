# 회장뽑기
from collections import deque

N = int(input())
lst = [[] for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break  # -1 -1이 입력되면 종료
    lst[a].append(b)
    lst[b].append(a)
# print(lst) # [[], [2], [1, 3, 4], [2, 4, 5], [3, 5, 2], [4, 3]]

arr = [[0] *(N+1) for _ in range(N+1)]
for n in range(1, N+1):
    for i in lst[n]:
        arr[n][i] = 1
# print(arr) # [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]

for n in range(1, N+1): # N번 돌거임
    for i in range(1, N+1): # 1번 친구부터
        queue = deque([])
        for j in range(1, N+1): # 친구 확인
            if arr[i][j] == n:
                queue.append(j)
        while queue:
            new_i = queue.popleft()
            for k in range(1, N+1):
                if i != k and arr[i][k] == 0:
                    if arr[new_i][k] == 1:
                        arr[i][k] = n + 1
# print(arr) # [[0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 2, 3], [0, 1, 0, 1, 1, 2], [0, 2, 1, 0, 1, 1], [0, 2, 1, 1, 0, 1], [0, 3, 2, 1, 1, 0]]
scores = [0]* (N+1)
for i in range(N+1):
    scores[i] = max(arr[i])
scores[0] = N
# print(scores) # [N, 3, 2, 2, 2, 3]

score = min(scores)
cnt = 0
king = []
for i in range(N+1):
    if scores[i] == score:
        cnt += 1
        king.append(i)
print(score, cnt)
print(*king)